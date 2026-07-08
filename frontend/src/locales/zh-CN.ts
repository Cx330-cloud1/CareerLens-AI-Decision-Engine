export default {
  navigation: {
    dashboard: "仪表盘",
    talentProfile: "简历智能",
    companyIntelligence: "公司情报",
    roleIntelligence: "岗位情报",
    matchReport: "匹配报告",
    careerPlan: "职业规划"
  },
  language: {
    label: "语言",
    zhCN: "中文",
    enUS: "English"
  },
  pages: {
    dashboard: {
      eyebrow: "仪表盘",
      title: "CareerLens 系统状态",
      backend: "后端：",
      connected: "已连接",
      disconnected: "未连接"
    },
    talentProfile: {
      eyebrow: "简历智能",
      title: "从简历证据到能力分析",
      lede: "上传简历或粘贴简历文本，生成结构化身份、能力、证据和改进建议。",
      upload: {
        title: "上传简历",
        description: "支持 PDF、TXT、Markdown、DOC、DOCX。当前基础流程会本地读取文本文件。",
        status: "输入状态",
        emptyStatus: "等待简历",
        readyStatus: "{name} 已就绪",
        textReadyStatus: "粘贴文本已就绪"
      },
      fields: {
        resumeText: {
          label: "简历文本",
          placeholder: "在此粘贴简历文本以预览证据抽取。PDF 会作为简历文件接收，详细 PDF 文本解析将在后续服务中接入。"
        }
      },
      actions: {
        analyze: "分析简历",
        analyzing: "分析中..."
      },
      report: {
        ariaLabel: "简历智能报告",
        candidateIdentity: "候选人身份",
        capabilities: "能力卡片",
        evidence: "经历证据",
        suggestions: "改进建议"
      },
      empty: {
        ariaLabel: "简历智能预览",
        title: "结构化简历智能",
        description: "上传简历或粘贴简历文本后，系统会生成能力卡、证据卡、置信度信号和下一步建议。"
      },
      errors: {
        analysisFailed: "简历分析失败。请确认后端服务已启动后重试。"
      }
    },
    companyIntelligence: {
      eyebrow: "公司情报",
      title: "公司与市场上下文",
      lede: "用于管理公司 DNA 与可溯源情报的基础页面。"
    },
    roleIntelligence: {
      eyebrow: "岗位情报",
      title: "岗位预期与评估信号",
      lede: "用于管理岗位模板、要求与评估信号的基础页面。"
    },
    matchReport: {
      eyebrow: "匹配报告",
      title: "可解释的匹配分析",
      lede: "用于管理评分维度、证据、假设与置信度的基础页面。"
    },
    careerPlan: {
      eyebrow: "职业规划",
      title: "行动计划与准备路径",
      lede: "用于管理与匹配差距相关的阶段性行动。"
    }
  }
};
