export default {
  navigation: {
    dashboard: "仪表盘",
    talentProfile: "人才画像",
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
      eyebrow: "人才画像",
      title: "结构化职业身份",
      lede: "用于沉淀画像数据、证据链与版本记录的基础页面。",
      fields: {
        education: {
          label: "教育背景",
          placeholder: "计算机科学硕士，某大学...\n数据分析证书..."
        },
        skills: {
          label: "技能",
          placeholder: "Python\nSQL\n市场研究\n利益相关方沟通"
        },
        projects: {
          label: "项目经历",
          placeholder: "搭建流失分析看板，将每周报告时间减少 40%..."
        },
        targetRoles: {
          label: "目标岗位",
          placeholder: "数据分析师\n产品分析师\n商业智能分析师"
        }
      },
      actions: {
        analyze: "分析画像",
        analyzing: "分析中..."
      },
      report: {
        ariaLabel: "人才画像报告",
        careerIdentity: "职业身份",
        capabilities: "能力图谱",
        evidence: "证据摘要",
        strengths: "优势",
        gaps: "差距",
        recommendedRoles: "推荐岗位"
      },
      empty: {
        ariaLabel: "报告预览",
        title: "结构化人才画像",
        description: "填写信息并运行分析，生成职业身份、能力图谱、证据摘要、优势、差距与推荐岗位。"
      },
      errors: {
        analysisFailed: "画像分析失败。请确认后端服务已启动后重试。"
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
