"use strict";
const $ = (id) => document.getElementById(id);
const typeNames = {single: "单选题", multiple: "多选题", judge: "判断题"};
const modeNames = {sequential: "顺序练习", random: "随机练习", mistakes: "错题复习"};
const storageKey = "ict-practice-session-v1";
let bank, stats, state, busy = false, toastTimer;
const token = () => {
  if (typeof crypto.randomUUID === "function") return crypto.randomUUID();
  const bytes = crypto.getRandomValues(new Uint8Array(16));
  return Array.from(bytes, byte => byte.toString(16).padStart(2, "0")).join("");
};

function emphasizeKeywords(element, text) {
  const keywords = /不正确|不属于|不支持|不包含|不包括|不可以|不能|错误|只有|必须|至少|最多|最少|最大|最小|缺省|默认|全部|\b(?:Router\s*ID|OSPFv3|OSPF|RSTP|MSTP|STP|VLANIF|VLAN|IPv6|IPv4|IP|TCP|UDP|ARP|DHCPv6|DHCP|CAPWAP|RADIUS|VRRP|BGP|IS-IS|MPLS|ACL|NAT|LACP|PPPoE|PPP|SSID|WLAN|SNMP|FTP|Telnet|MAC|BPDU|DR|BDR)\b/gi;
  const fragment = document.createDocumentFragment();
  let position = 0;
  for (const match of text.matchAll(keywords)) {
    fragment.append(document.createTextNode(text.slice(position, match.index)));
    const strong = document.createElement("strong");
    strong.className = "question-keyword";
    strong.textContent = match[0];
    fragment.append(strong);
    position = match.index + match[0].length;
  }
  fragment.append(document.createTextNode(text.slice(position)));
  element.replaceChildren(fragment);
}

async function api(path, body) {
  if (window.ICTOffline) return window.ICTOffline.request(path, body);
  const response = await fetch(path, body ? {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(body)} : {});
  let result;
  try { result = await response.json(); } catch { throw new Error("无法读取服务返回的数据，请检查本地服务。"); }
  if (!response.ok) throw new Error(result.error || "请求失败，请稍后重试。");
  return result;
}
function toast(message) {
  $("toast").textContent = message;
  $("toast").hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { $("toast").hidden = true; }, 4200);
}
function persist() {
  try { localStorage.setItem(storageKey, JSON.stringify(state)); }
  catch { toast("浏览器暂时无法保存当前位置，作答记录仍会保存在本机。"); }
}
function shuffle(items) {
  const list = [...items];
  for (let i = list.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [list[i], list[j]] = [list[j], list[i]];
  }
  return list;
}
function syncSettings() {
  $("type-filter").value = state.filters.type;
  $("topic-filter").value = state.filters.topic;
  $("random-count").value = state.filters.count;
  $("include-mastered").checked = state.filters.includeMastered;
}
function newSession(mode = state?.mode || "sequential", filters = null) {
  if (busy) return toast("正在保存这次作答，请稍候。");
  filters ||= {type: $("type-filter").value, topic: $("topic-filter").value,
    count: $("random-count").value, includeMastered: $("include-mastered").checked};
  let questions = bank.questions.filter(q => (filters.type === "all" || q.type === filters.type) &&
    (filters.topic === "all" || q.topic === filters.topic));
  if (mode === "mistakes") {
    const wrongIds = new Set(stats.mistakes.filter(q => filters.includeMastered || !q.mastered).map(q => q.id));
    questions = questions.filter(q => wrongIds.has(q.id));
  }
  let queue = questions.map(q => q.id);
  if (mode === "random") {
    queue = shuffle(queue);
    if (filters.count !== "all") queue = queue.slice(0, Number(filters.count));
  }
  state = {version: bank.version, mode, filters, queue, position: 0, entries: {}, completed: false};
  persist(); syncSettings(); render();
}
function currentQuestion() { return bank.questions.find(q => q.id === state.queue[state.position]); }
function entry() {
  const key = String(state.position);
  state.entries[key] ||= {token: token(), selected: [], feedback: null};
  return state.entries[key];
}
async function updateStats() {
  stats = await api("/api/stats");
  const waiting = stats.mistakes.filter(q => !q.mastered).length;
  $("stat-total").textContent = bank.questions.length;
  $("stat-practiced").textContent = `${stats.practiced} 题`;
  $("stat-rate").textContent = stats.attempts ? `${Math.round(stats.correct / stats.attempts * 100)}%` : "—";
  $("stat-mistakes").textContent = `${waiting} 题`;
  $("mistake-count").textContent = waiting;
  $("stat-progress-note").textContent = `还有 ${bank.questions.length - stats.practiced} 道题未练习`;
}
function render() {
  for (const button of document.querySelectorAll("[data-mode]")) {
    const active = button.dataset.mode === state.mode;
    button.classList.toggle("active", active);
    button.setAttribute("aria-current", active ? "page" : "false");
  }
  $("breadcrumb-mode").textContent = modeNames[state.mode];
  $("session-label").textContent = modeNames[state.mode];
  $("random-settings").hidden = state.mode !== "random";
  $("mastered-setting").hidden = state.mode !== "mistakes";
  const titles = {sequential: "按自己的节奏，逐题掌握。", random: "打乱顺序，检验真正的理解。", mistakes: "把曾经的错题，变成会的题。"};
  $("page-title").textContent = titles[state.mode];
  $("page-subtitle").textContent = state.mode === "mistakes" ? "每个薄弱点，都值得再给自己一次机会。" : "从基础到进阶，每一次选择都有答案，也有解释。";
  const empty = !state.queue.length || state.completed;
  $("question-card").hidden = empty;
  $("empty-state").hidden = !empty;
  $("question-card").setAttribute("aria-busy", "false");
  if (empty) {
    $("session-progress").textContent = state.completed ? `本轮 ${state.queue.length} 题已完成` : "0 题";
    $("progress-fill").style.width = state.completed ? "100%" : "0%";
    if (state.completed) {
      const results = Object.values(state.entries).filter(e => e.feedback);
      const correct = results.filter(e => e.feedback.correct).length;
      $("empty-title").textContent = "本轮练习完成！";
      $("empty-description").textContent = `共 ${state.queue.length} 题，答对 ${correct} 题，跳过 ${state.queue.length - results.length} 题。答错的题已自动加入错题本。`;
      $("empty-action").textContent = "再练一轮";
    } else {
      $("empty-title").textContent = state.mode === "mistakes" ? "当前没有待复习的错题" : "当前条件下没有题目";
      $("empty-description").textContent = state.mode === "mistakes" ? "可以继续练新题，或勾选“包含已掌握的错题”。" : "试着选择全部题型或全部知识点。";
      $("empty-action").textContent = "开始顺序练习";
    }
    return;
  }
  const q = currentQuestion(), attempt = entry(), feedback = attempt.feedback;
  $("session-progress").textContent = `${state.position + 1} / ${state.queue.length}`;
  $("progress-fill").style.width = `${(state.position + Number(Boolean(feedback))) / state.queue.length * 100}%`;
  $("question-type").textContent = typeNames[q.type];
  $("question-topic").textContent = q.topic;
  $("question-number").textContent = `原题 #${String(q.id).padStart(3, "0")}`;
  emphasizeKeywords($("question-stem"), q.stem);
  $("question-figure").hidden = !q.image;
  if (q.image) {
    $("question-image").src = q.image.src;
    $("question-image").alt = q.image.alt;
    $("figure-caption").textContent = q.image.caption;
  } else {
    $("question-image").removeAttribute("src");
    $("question-image").alt = "";
  }
  $("selection-hint").textContent = q.type === "multiple" ? "选择所有正确选项，再点击“确认答案”。" : "选择一个答案，即刻查看对错与解析。";
  $("options").replaceChildren();
  const legend = document.createElement("legend");
  legend.className = "sr-only"; legend.textContent = "选择答案"; $("options").append(legend);
  for (const [letter, text] of Object.entries(q.options)) {
    const label = document.createElement("label"); label.className = "option";
    const input = document.createElement("input");
    input.type = q.type === "multiple" ? "checkbox" : "radio";
    input.name = "answer"; input.value = letter; input.checked = attempt.selected.includes(letter);
    input.disabled = busy || Boolean(feedback);
    const marker = document.createElement("span"); marker.className = "option-letter"; marker.textContent = letter;
    const content = document.createElement("span"); content.className = "option-text"; emphasizeKeywords(content, text);
    label.append(input, marker, content);
    label.classList.toggle("selected", input.checked);
    if (feedback) {
      label.classList.add("locked");
      if (feedback.answer.includes(letter)) {
        label.classList.add("correct");
        const result = document.createElement("span"); result.className = "option-result"; result.textContent = "正确选项 ✓"; label.append(result);
      } else if (input.checked) {
        label.classList.add("wrong");
        const result = document.createElement("span"); result.className = "option-result"; result.textContent = "你的选择 ×"; label.append(result);
      }
    }
    input.addEventListener("change", () => {
      if (busy || attempt.feedback) return;
      if (q.type === "multiple") {
        attempt.selected = [...$("options").querySelectorAll("input:checked")].map(el => el.value);
        label.classList.toggle("selected", input.checked);
        $("submit").disabled = !attempt.selected.length;
        persist();
      } else {
        attempt.selected = [letter]; persist(); submitAnswer();
      }
    });
    $("options").append(label);
  }
  $("submit").hidden = q.type !== "multiple" || Boolean(feedback);
  $("submit").disabled = busy || !attempt.selected.length;
  $("retry").hidden = !feedback;
  $("retry").disabled = busy;
  $("save-status").textContent = busy ? "正在判分并保存…" : feedback ? "作答已保存" : "";
  $("feedback").hidden = !feedback;
  if (feedback) {
    $("feedback").classList.toggle("incorrect", !feedback.correct);
    $("feedback-title").textContent = feedback.correct ? "✓ 回答正确" : "再想一想，已加入错题本";
    $("feedback-answer").textContent = `你的答案：${feedback.selected.join("、")}　正确答案：${feedback.answer.join("、")}`;
    $("explanation").textContent = feedback.explanation;
    $("source-links").replaceChildren();
    feedback.sources.forEach((url, index) => {
      if (!/^https:\/\//.test(url)) return;
      const a = document.createElement("a"); a.href = url; a.target = "_blank"; a.rel = "noopener noreferrer";
      a.textContent = `参考依据 ${index + 1} ↗`; $("source-links").append(a);
    });
  }
  $("previous").disabled = busy || state.position === 0;
  $("next").disabled = busy;
  $("next").textContent = state.position === state.queue.length - 1 ? "完成本轮 ✓" : feedback ? "下一题 →" : "跳过 →";
  $("footer-hint").textContent = q.type === "multiple" ? "多选题需要确认后判分" : "选择后自动判分";
}
async function submitAnswer() {
  if (busy || !state || !state.queue.length || entry().feedback || !entry().selected.length) return;
  busy = true; render();
  const attempt = entry();
  try {
    const feedback = await api("/api/answer", {token: attempt.token, question_id: currentQuestion().id, selected: attempt.selected});
    attempt.feedback = feedback;
    persist();
    try { await updateStats(); } catch { toast("答案已保存，统计暂时无法更新。"); }
  } catch (error) {
    // A failed single-choice submission must remain retryable by clicking again.
    if (currentQuestion().type !== "multiple") attempt.selected = [];
    persist(); toast(error.message);
  } finally { busy = false; render(); }
}
function advance(delta) {
  if (busy || !state || !state.queue.length) return;
  if (delta > 0 && state.position === state.queue.length - 1) state.completed = true;
  else state.position = Math.max(0, Math.min(state.queue.length - 1, state.position + delta));
  persist(); render();
  document.querySelector(".practice-layout")?.scrollIntoView({block: "start", behavior: "smooth"});
}
$("submit").addEventListener("click", submitAnswer);
$("previous").addEventListener("click", () => advance(-1));
$("next").addEventListener("click", () => advance(1));
$("retry").addEventListener("click", () => {
  if (busy) return;
  state.entries[String(state.position)] = {token: token(), selected: [], feedback: null}; persist(); render();
});
$("restart").addEventListener("click", () => { if (bank && state) newSession(); });
$("apply-settings").addEventListener("click", () => { if (bank && state) newSession(); });
$("empty-action").addEventListener("click", () => {
  if (!bank || !state) return;
  if (state.completed) newSession(state.mode);
  else newSession("sequential", {type: "all", topic: "all", count: "20", includeMastered: false});
});
for (const button of document.querySelectorAll("[data-mode]")) {
  button.addEventListener("click", () => { if (bank && button.dataset.mode !== state.mode) newSession(button.dataset.mode); });
}
$("export-toggle").addEventListener("click", () => {
  $("export-menu").hidden = !$("export-menu").hidden;
  $("export-toggle").setAttribute("aria-expanded", String(!$("export-menu").hidden));
});
document.addEventListener("click", event => {
  if (!$("export-menu").contains(event.target) && event.target !== $("export-toggle")) {
    $("export-menu").hidden = true; $("export-toggle").setAttribute("aria-expanded", "false");
  }
});
document.addEventListener("keydown", event => {
  if (event.key === "Escape") { $("export-menu").hidden = true; $("export-toggle").setAttribute("aria-expanded", "false"); }
});
async function init() {
  try {
    bank = await api("/api/questions"); await updateStats();
    for (const topic of [...new Set(bank.questions.map(q => q.topic))].sort((a,b) => a.localeCompare(b, "zh-CN"))) {
      const option = document.createElement("option"); option.value = topic; option.textContent = topic; $("topic-filter").append(option);
    }
    const summary = bank.summary;
    $("bank-note").append(document.createTextNode(`原题 ${summary.source_count} 道 · 去重 ${summary.duplicate_count} 道 · 剔除残缺或存疑 ${summary.invalid_count} 道 · 全部保留题已配解析。 `));
    const report = document.createElement("a"); report.href = "/exports/cleaning.md"; report.textContent = "查看清理与修正报告 ↗"; $("bank-note").append(report);
    let saved;
    try { saved = JSON.parse(localStorage.getItem(storageKey)); } catch { saved = null; }
    const ids = new Set(bank.questions.map(q => q.id));
    const validSaved = saved && saved.version === bank.version && Object.hasOwn(modeNames, saved.mode) &&
      saved.filters && Object.hasOwn(saved.filters, "type") && Object.hasOwn(saved.filters, "topic") &&
      Array.isArray(saved.queue) && saved.queue.every(id => ids.has(id)) && new Set(saved.queue).size === saved.queue.length &&
      Number.isInteger(saved.position) && saved.position >= 0 && saved.position < Math.max(1, saved.queue.length) && saved.entries;
    if (validSaved) { state = saved; syncSettings(); render(); }
    else newSession("sequential", {type: "all", topic: "all", count: "20", includeMastered: false});
  } catch (error) {
    $("question-stem").textContent = "练习室暂时无法打开";
    $("selection-hint").textContent = `${error.message} 请确认启动窗口仍在运行，然后刷新页面。`;
    $("question-card").setAttribute("aria-busy", "false");
    toast(error.message);
  }
}
init();
