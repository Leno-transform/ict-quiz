/* Standalone storage and grading.
   Two modes:
   - single-file build: the bank is embedded in <script id="ict-bank">;
   - hosted build: the bank is loaded from ./questions.json and images from ./assets/.
   Both keep practice records in localStorage and grade client-side. */
"use strict";
(() => {
  const embeddedElement = document.getElementById("ict-bank");
  const recordsKey = "ict-mobile-records-v1";
  const boot = (async () => {
    const data = embeddedElement
      ? JSON.parse(embeddedElement.textContent)
      : await (await fetch("./questions.json", {cache: "no-store"})).json();
    return {data, questions: new Map(data.questions.map(q => [q.id, q]))};
  })();
  function readRecords() {
    const raw = localStorage.getItem(recordsKey);
    if (!raw) return {attempts: {}, progress: {}};
    const records = JSON.parse(raw);
    if (!records.attempts || !records.progress) throw new Error("练习记录格式损坏，请先导出备份。");
    return records;
  }
  function mobileStats(records, questions) {
    const attempts = Object.values(records.attempts).filter(a => questions.has(a.question_id));
    return {attempts: attempts.length, correct: attempts.filter(a => a.correct).length,
      practiced: new Set(attempts.map(a => a.question_id)).size,
      mistakes: Object.entries(records.progress).filter(([id, p]) => questions.has(Number(id)) && p.wrong_count > 0)
        .map(([id, p]) => ({id: Number(id), wrong_count: p.wrong_count, mastered: p.right_streak >= 2}))
        .sort((a, b) => b.wrong_count - a.wrong_count)};
  }
  window.ICTOffline = {
    embedded: Boolean(embeddedElement),
    async request(path, body) {
      const {data, questions} = await boot;
      if (path === "/api/questions") return data;
      const records = readRecords();
      if (path === "/api/stats") return mobileStats(records, questions);
      if (path !== "/api/answer") throw new Error("不支持的操作。");
      const q = questions.get(body.question_id);
      if (!q || !Array.isArray(body.selected) || !body.selected.length ||
          body.selected.some(v => typeof v !== "string" || (q.type === "fill" ? !v.trim() || v.trim().length > 200 : !Object.hasOwn(q.options, v))) ||
          new Set(body.selected).size !== body.selected.length ||
          (q.type !== "multiple" && body.selected.length !== 1)) throw new Error("请选择有效的答案。");
      const selected = q.type === "fill" ? [body.selected[0].trim()] : [...body.selected].sort();
      const old = records.attempts[body.token];
      if (old) {
        if (old.question_id !== q.id || JSON.stringify(old.selected) !== JSON.stringify(selected))
          throw new Error("这次答案已提交，请使用“重新作答”。");
        return old;
      }
      const correct = selected.join("") === [...q.answer].sort().join("");
      const feedback = {question_id: q.id, correct, selected, answer: [...q.answer], explanation: q.explanation, sources: q.sources};
      records.attempts[body.token] = {...feedback, created_at: Date.now()};
      const previous = records.progress[q.id] || {wrong_count: 0, right_streak: 0};
      records.progress[q.id] = {wrong_count: previous.wrong_count + Number(!correct),
        right_streak: correct ? previous.right_streak + 1 : 0};
      try { localStorage.setItem(recordsKey, JSON.stringify(records)); }
      catch { throw new Error("手机存储不可用或已满，请退出隐私浏览模式，或先导出记录备份。"); }
      return feedback;
    }
  };
  function downloadFile(bytes, name, mime) {
    const blob = new Blob([bytes], {type: mime});
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a"); link.href = url; link.download = name;
    document.body.append(link); link.click(); link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 60000);
  }
  function reportStatus(message) {
    const status = document.getElementById("mobile-status");
    if (status) status.textContent = message;
  }
  function downloadRecords() {
    boot.then(({data}) => {
      downloadFile(JSON.stringify({version: data.version, ...readRecords()}, null, 2), "ICT学习记录.json", "application/json");
    }).catch(error => reportStatus(error.message));
  }
  const menuLinks = [...document.querySelectorAll("#export-menu a")];
  if (window.ICTOffline.embedded) {
    // The single-file build carries the exports inside itself, so links are served from memory.
    menuLinks.forEach(link => {
      link.addEventListener("click", async event => {
        event.preventDefault();
        try {
          const path = link.getAttribute("href");
          const {data} = await boot;
          if (path === "/api/backup") {
            const records = readRecords();
            downloadFile(JSON.stringify({version: data.version, ...records}, null, 2), "ICT手机学习记录.json", "application/json");
          } else if (path === "/exports/questions.json") {
            downloadFile(JSON.stringify(data, null, 2), "ICT题库及解析.json", "application/json");
          } else if (path === "/exports/explanations.md") {
            const text = JSON.parse(document.getElementById("ict-explanations").textContent);
            downloadFile(text, "ICT题库及解析.md", "text/markdown;charset=utf-8");
          } else if (path === "/exports/cleaning.md") {
            downloadFile(JSON.parse(document.getElementById("ict-cleaning").textContent), "ICT题库清理报告.md", "text/markdown;charset=utf-8");
          } else {
            const base64 = document.getElementById("ict-materials").textContent.trim();
            downloadFile(Uint8Array.from(atob(base64), c => c.charCodeAt(0)), "ICT题库资料.zip", "application/zip");
          }
        } catch (error) { reportStatus(error.message); }
      });
    });
  } else {
    // The hosted build ships the exports as real files; only the personal record needs generating.
    menuLinks.filter(link => link.dataset.export === "backup").forEach(link => {
      link.addEventListener("click", event => { event.preventDefault(); downloadRecords(); });
    });
  }
  document.addEventListener("click", event => {
    if (event.defaultPrevented) return;
    if (event.target instanceof HTMLAnchorElement && event.target.getAttribute("href") === "/exports/cleaning.md") {
      event.preventDefault();
      if (window.ICTOffline.embedded) {
        downloadFile(JSON.parse(document.getElementById("ict-cleaning").textContent), "ICT题库清理报告.md", "text/markdown;charset=utf-8");
      } else {
        location.href = "./exports-cleaning.md";
      }
    }
  });
  let installEvent;
  const install = document.getElementById("mobile-install");
  window.addEventListener("beforeinstallprompt", event => {
    event.preventDefault(); installEvent = event; install.hidden = false;
  });
  install?.addEventListener("click", async () => {
    if (installEvent) { await installEvent.prompt(); installEvent = null; install.hidden = true; }
  });
  if (location.protocol === "file:") {
    reportStatus("独立文件版 · 题库与图片已内置，无需电脑或网络。");
  } else if ("serviceWorker" in navigator && window.isSecureContext) {
    let ready = false;
    const markReady = () => {
      if (ready) return;
      ready = true;
      reportStatus("离线就绪 · 可添加到主屏幕，电脑关机后仍可练习。");
      document.getElementById("mobile-status")?.classList.add("mobile-ready");
    };
    reportStatus("正在准备离线题库，请等待显示“离线就绪”后再断网。");
    navigator.serviceWorker.register("./sw.js", {updateViaCache: "none"}).then(() => {
      // The worker precaches the bank and every figure before it claims this page,
      // so a controller means the offline copy is complete.
      if (navigator.serviceWorker.controller) return markReady();
      navigator.serviceWorker.addEventListener("controllerchange", markReady, {once: true});
      setTimeout(() => { if (!ready) reportStatus("题库已缓存；图片仍在后台缓存，稍后刷新即可完全断网。"); }, 45000);
    }).catch(() => { reportStatus("当前离线准备失败；联网刷新一次即可缓存题库与图片。"); });
  } else reportStatus("当前可独立练习；添加到主屏幕和离线安装需要 HTTPS 网址。");
})();
