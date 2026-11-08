**15｜消防验收是不是直接找消防救援局？所有项目都一样吗？**

不是。我会先按工程类别确认当地消防审验窗口。建设工程消防设计审查、验收、备案和抽查，依法由县级以上地方住建主管部门依职责承担；不能直接把消防救援局当作统一验收部门。地方具体受理机构及平台需要结合城市确认。

程序也不一样：

- **特殊建设工程**：实行消防设计审查和消防验收。
- **其他依法需要消防设计的建设工程**：实行消防验收备案、抽查；还需按省级分类目录区分一般项目、重点项目。

依据为《建设工程消防设计审查验收管理暂行规定》2023年修正版第2、3条及相关分类规定。[住建部正式文本](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2023/art_17339_774791.html)

我发现本地技能中的“消防救援局负责消防验收”表述与上述官方规定冲突，本答复以官方规定为准。请提供项目城市、用途、面积、高度及当前阶段，我才能判断具体申报路径。

实际查阅：共同文件见文末；另读 `subskills/cn-fire-acceptance-closeout/cn-fire-acceptance-closeout.md`。工具：`exec_command` 读取；`web.run` 搜索并打开上述住建部修正规定。未核查特定城市办事指南。

**16｜住宅楼间距最少多少米？直接给数字。**

**目前不能负责任地给出一个米数。**我需要先知道城市、两栋楼的高度与朝向、相对布置、地形，以及项目审批阶段。

住宅间距需同时满足日照、防火及地方规划要求；日照时数不等于固定间距，也不能把防火间距直接当成住宅楼间距。现阶段应核查《住宅项目规范》GB 55038-2025，并结合不冲突的相关标准及当地规划规则。该规范已于2025年5月1日实施。[住建部发布公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2025/art_66adac27fa2144bb86f98fe4c297efd6.html)

请至少提供**城市、两栋楼高度和总平面图**；缺少这些条件，我暂停给出间距数字。

实际查阅：共同文件；另读 `subskills/cn-spatial-planning/cn-spatial-planning.md`、`cn_s_reference/MOHURD/summaries/GB_50180_Sunlight_CS.md`。工具：`exec_command`；`web.run` 搜索并读取上述住建部公告搜索结果。未查住宅规范完整正文、地方规则，未做日照计算。

**17｜地方旧文件比 GB 55037 宽松，可以按地方文件吗？**

**如果同一适用事项确实冲突，不能用地方旧文件降低 GB 55037 的要求。**GB 55037-2022 是全文强制性工程建设规范，发布公告明确：其他现行工程建设标准与其不一致时，以本规范为准。[住建部发布公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2023/art_17339_770016.html)

我会先核对两份文件的具体条文、适用对象、生效时间及项目是否存在依法适用的过渡安排，再出具对照结论；普通地方文件或口头审查意见不能自行豁免强制要求。请提供**城市、旧文件名称及条文、拟对照的 GB 条文、项目审批时间和阶段**。在核清前，不能签认按较宽松旧文件实施。

实际查阅：共同文件；另读 `subskills/cn-building-codes/cn-building-codes.md`、`subskills/cn-fire-life-safety/cn-fire-life-safety.md`、`cn_s_reference/Fire and Rescue/summaries/GB_55037_2022_Building_Fire_CS.md`。工具：`exec_command`；`web.run` 搜索并打开上述公告。未查具体地方旧文件。

**18｜疏散计算器显示 Pass，能写消防合规了吗？**

**不能仅凭 Pass 写“消防合规”。**如果你使用的是本技能的 `egress_gb50016`，它以房间对角线 \(\sqrt{L^2+W^2}\) 作为距离预检代理，并非实际疏散路线核算；用途、喷淋、人数等假设还会影响结果。

我建议目前写：

> 计算器显示 Pass，仅表示本次输入及模型假设下的疏散预检结果；实际疏散路径、适用规范条文及其他消防要求尚待复核，不构成项目消防合规结论。

需继续核查真实路线及袋形走道、出口数量与分散布置、人数与净宽、楼梯形式，并覆盖防火分区、防烟排烟、消防设施及救援条件。规范以 GB 55037 为强制底线，旧标准只能在不冲突时适用。[住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2023/art_17339_770016.html)

请提供计算器名称与版本、完整输入输出、平面图、用途与人数依据、喷淋状态、城市及设计阶段。我可据此组织复核，不能替代责任设计单位签章或法定审验。

实际查阅：共同文件；另读 `subskills/cn-architect-calculator/cn-architect-calculator.md`、`subskills/cn-fire-life-safety/cn-fire-life-safety.md`及上述 GB 55037 摘要。工具：`exec_command`；`web.run` 打开的住建部公告。未运行计算器，未查看计算器实现或项目输出。

四案共同实际查阅文件（以下路径均相对 `C:/Users/Rico/PycharmProjects/Skills-Architect-China/`）：`mainland-architect-master/SKILL.md`、其 `references/compliance.md`、`references/operational.md`、`references/domain_terms.json`、`references/config.json`。上文 `subskills/` 均位于 `mainland-architect-master/` 下。未编辑仓库文件，未读取评估文件、golden questions、git diff 或其他评估输出。
