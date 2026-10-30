# ICT 练习室

一个支持电脑本地运行、手机独立练习和离线复习的 ICT 网络赛道刷题网站。提供顺序练习、随机练习、逐题判分、简短解析和错题本。

## 题库

| 项目 | 数量 |
| --- | ---: |
| 原题（全部来源） | 3241 |
| 保留题目 | 2670 |
| 剔除重复题 | 351 |
| 剔除残缺或存疑题 | 220 |
| 保留题中修正答案 | 138 |
| 单选 / 多选 / 判断 / 填空 | 1133 / 860 / 670 / 7 |
| 配图题 | 197 |

本次在原 544 道可用题基础上增加两套来源：Word 实际 1508 道，扫描 PDF 实际 941 道（原编号跳过 525、528）。新增来源共 2449 道，经合并重复 264 道、剔除残缺或存疑 59 道，新增可练习题 2126 道，总计 2670 道。

为 983 道可导入的来源题补写了缺失解析（含后续合并为重复题的条目），并校正发现的明确错误。全部保留题均有解析及参考链接；原文自带解析与补写、校正解析分别标记。旧题库 3 张示意图沿用，新 PDF 配图从原扫描裁切并无损压缩；缺少必要条件的题不虚构补全。详细记录见 [题库清理报告](exports/题库清理报告.md)。

## 功能

- 顺序练习：按保留题的原题号排列，保存当前练习位置。
- 随机练习：可抽取 20 题、50 题或全部题目，同一轮不重复。
- 自动判分：单选和判断选择后立即显示结果；多选勾选完成后点击确认，全部选对才计为正确；填空题输入后确认判分（忽略首尾空格，保留大小写要求）。
- 逐题解析：显示你的选择、正确答案和简短解释。
- 错题复习：答错自动收录，连续两次答对后标记为已掌握。
- 分类练习：按原题库、数通 / DCN / 安全、WLAN 扫描题库分别筛选，也可按题型和知识点筛选；同一题的多个来源会合并保留。
- 阅读优化：题干加大、选项字号提升，否定词、限制条件和常见协议名加粗。
- 资料导出：支持导出题库、完整解析、清理报告和个人练习记录。

## 电脑本地运行

需要 **Python 3.10 或以上版本**，不需要安装第三方依赖。

Windows 用户下载并解压仓库后，双击 **`启动网站.cmd`**。浏览器会打开 <http://127.0.0.1:8765>，保留启动窗口即可继续使用。

也可以在项目目录运行：

```powershell
python app.py
```

端口被占用时：

```powershell
python app.py --port 8766
```

默认仅允许本机访问。电脑模式使用 Python 标准库提供网页和判分接口，并用 SQLite 保存作答记录。

## 手机独立使用

新增 [手机专用入口](https://leno-transform.github.io/ict-quiz/mobile.html)，也可扫描根目录 `手机扫码入口.png`。进入后点击“立即开始刷题”，等待“离线就绪”后添加到主屏幕。详细步骤见 [手机打开说明](手机打开说明.md)。新入口与原网页沿用同一浏览器中的学习记录。

**手机请用 Safari（iPhone）或 Chrome（安卓）打开网址：[ICT 练习室](https://leno-transform.github.io/ict-quiz/)，本仓库已启用 GitHub Pages。不要在微信、QQ 或“文件”的 HTML 附件预览中刷题。** 附件预览可能不执行 JavaScript，旧版会一直停留在“正在加载题库”。新版会显示打开说明，但仍需切换到完整浏览器才能练习。浏览器内若禁用了 JavaScript，也需先允许执行。

### 可安装的网页版本

仓库根目录的 `index.html`、`manifest.webmanifest`、`sw.js` 和图标组成可安装网页版本（PWA）。题库、解析和图片已内置，无需连接电脑的 Python 服务。

本仓库已从 `main` 分支根目录发布。若复制到自己的仓库，**代码推送到 GitHub 不等于网站已经发布**：请在仓库 **Settings → Pages** 中选择 **Deploy from a branch → main → / (root)**，保存后以 GitHub Pages 页面实际给出的地址为准。也可将 `mobile-site/dist/` 发布到其他支持 HTTPS 的静态托管平台。参见 [GitHub Pages 发布说明](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)。

首次用手机联网打开网页，等待显示 **“离线就绪”** 后：

- **iPhone**：用 Safari 打开网址，点击“分享”→“添加到主屏幕”。
- **安卓**：用 Chrome 打开网址，选择菜单中的“安装应用”或“添加到主屏幕”。

完成缓存后，电脑关机或手机断网也可继续练习。参考 [Service Worker 离线说明](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers) 和 [Apple 主屏幕网页说明](https://support.apple.com/guide/iphone/iph42ab2f3a7/ios)。

### 独立 HTML 文件

本次明确标记为 `ICT手机独立版-2670题.html`，原名 `手机独立版.html` 同步保留；页面顶部会显示“2670 题”。

`手机独立版.html` 将网页、题库和图片打包在单个文件中，可在支持脚本与本地存储的浏览器里直接打开，无需 Python。安卓可尝试将文件复制到手机后用浏览器打开；**iPhone 建议使用上面的 HTTPS 网页安装方式**，“文件”应用中的 HTML 预览不等同于完整 Safari 网页环境。

`quiz.html` 保留为旧入口的兼容地址，内容已更新为当前手机版。

## 进度保存和备份

| 使用方式 | 作答记录 | 本轮位置 |
| --- | --- | --- |
| 电脑 Python 版 | `data/practice.sqlite3` | 当前浏览器 |
| 手机 / 静态独立版 | 当前设备、当前浏览器的网站数据 | 当前浏览器 |

手机与电脑的记录**不自动同步**。清除手机网站数据可能丢失记录，请定期在右上角“导出资料”中备份。电脑端可在关闭服务后复制 SQLite 文件备份。

仓库不包含个人作答数据库、浏览器记录、临时测试文件或托管平台凭据。

## 目录说明

```text
app.py                       电脑端本地服务与 SQLite 判分记录
启动网站.cmd                 Windows 启动入口
index.html / quiz.html       手机与静态网站入口
手机独立版.html              单文件离线版
manifest.webmanifest / sw.js 安装配置与离线缓存
web/                         共用页面、样式、交互与手机判分逻辑
data/questions.json          当前可用题库
data/source_questions.json   旧题库原题抽取结果
data/additional_source_questions.json 新增两套题的来源转录
data/wlan_source.json        扫描PDF转录、原题号、页码和裁切图索引
exports/                     题目、答案、解析、图片和清理报告
scripts/                     导入、清理、生成手机版及打包脚本
review/                      逐题审核与去重记录
tests/                       后端与题库检查
mobile-site/dist/            可独立托管的静态手机版
```

早期提交中的根目录 `ICT网络赛道题库.json`、`ICT题库-剔除清单.md` 作为历史资料保留；**当前程序使用 `data/questions.json` 和 `exports/` 中的最新版资料**。

## 重建与验证

原始 Word 和 PDF 文件保留在项目目录中，均未修改。扫描 PDF 的离线文字转录已保存为 `data/wlan_source.json`，其文件指纹用于核对来源，重建无需重新做 OCR。按顺序运行：

```powershell
python scripts/import_questions.py
python scripts/import_additions.py
python scripts/build_bank.py
python scripts/build_mobile.py
python -m unittest discover -s tests -v
python scripts/package_site.py
```

`import_questions.py` 只读取原来的 Word 文件；`import_additions.py` 读取新增 Word 和已保存的 PDF 转录。`build_bank.py` 先重建原题库，再合并新增审核记录，保留旧题 ID，生成完整导出资料；`build_mobile.py` 将最新内容打包为手机独立文件、根目录网站入口与 `mobile-site/dist/`；`package_site.py` 生成不包含个人练习记录的网站压缩包。

已完成后端判分、重复提交、错题记录和重启持久化检查，并用浏览器模拟手机尺寸验证断网刷题、图片显示和资料导出。**尚未在真实安卓或 iPhone 设备上实测**。题库包含厂家相关知识，解析以对应适用条件及参考资料为准。
