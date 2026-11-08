# 爆款研究实验室 · Viral Copy Lab

用于电商短视频的样本拆解、产品脚本生成和投放复盘的中文 AI Skill。技术名称为 `viral-copy-lab`，原技能界面名称为“爆款文案实验室”。

## 能做什么

- 从 Markdown/Obsidian 笔记提取视频链接，整理样本、开头、痛点与证据链。
- 根据产品、人群、卖点和拍摄条件生成可测试脚本与分镜。
- 结合发布数据复盘，积累有适用边界的爆款框架。
- 附带产品需求、待拆解视频 Markdown 模板，以及六张工作表的空白 Excel 模板。

## 安装到 Codex

下载本仓库 ZIP 并解压，将文件夹命名为 `viral-copy-lab`，放到项目中的 `.agents/skills/` 或个人的 `~/.agents/skills/` 下。安装后应存在 `viral-copy-lab/SKILL.md`，并完整保留同级的 `references/`、`scripts/`、`assets/` 和 `agents/` 目录。已有同名技能时，先备份并比较内容，避免直接覆盖。

也可在目标项目中运行（目标文件夹必须尚不存在）：

```sh
mkdir -p .agents/skills
git clone https://github.com/xiaoba88657-dotcom/viral-copy-lab.git .agents/skills/viral-copy-lab
```

安装目录说明见 [OpenAI 官方文档](https://developers.openai.com/api/reference/cli)。安装后开启新对话，并明确调用 `$viral-copy-lab`。

## 使用示例

```text
使用 $viral-copy-lab 拆解以下视频链接，区分可见事实和待验证推断。

使用 $viral-copy-lab，根据我提供的产品卖点、人群和棚拍条件，生成 5 条脚本，每条只测试一个主要变量。

使用 $viral-copy-lab，比较这批视频的曝光、3秒留存、完播、点击和支付数据，提出下一轮测试建议。
```

使用 Obsidian 时，提供自己的 vault 路径和待分析文件；建议入口为 `爆款研究/00-待拆解视频/`。不使用 Obsidian 时，可以直接提供链接、Markdown 文件或产品资料。

## 链接提取工具

Python 3.9+，仅使用标准库，无需额外依赖：

```sh
python3 scripts/extract_video_links.py path/to/notes.md
python3 scripts/extract_video_links.py path/to/notes --format tsv
```

脚本只做原始链接提取和去重，不联网、不解析短链、不下载视频；同一视频不同短链的最终去重需要在分析时完成。视频读取、联网、Obsidian 文件访问和 Excel 生成取决于所用 AI 环境提供的工具与权限。

## 文件结构

- `SKILL.md`：入口、模式和交付规则。
- `references/`：视频拆解、产品采集、脚本生成、框架与 Obsidian 工作流。
- `scripts/extract_video_links.py`：链接提取工具。
- `assets/`：空白 Markdown 与 Excel 模板。
- `agents/openai.yaml`：技能界面元数据。

## 公开内容范围

本仓库只发布技能工作流、工具和空白模板，不包含个人笔记、客户资料或历史投放数据。公开副本已移除作者个人电脑路径及系统隐藏文件。使用时只提供有权处理的素材，输出须区分事实、规律与推断，无法取得视频内容时不要编造分析。
