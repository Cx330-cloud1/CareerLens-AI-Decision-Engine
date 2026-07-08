# CareerLens User Flow

## 1. Product Experience Model

CareerLens should feel like a structured talent-role alignment workspace. The user should not land in an empty chat window. The primary experience is a guided SaaS workflow that turns a resume and target role into capability intelligence, role intelligence, an explainable alignment report, resume optimization guidance, and a development plan.

The core workflow is:

```text
Resume Upload
  -> Resume Intelligence
  -> Talent Capability Graph
  -> Role Intelligence
  -> Talent-Role Alignment Report
  -> Resume Optimization
  -> Career Development Plan
```

## 2. Primary Navigation

Recommended main navigation:

- Home
- Resume Intelligence
- Capability Graph
- Role Intelligence
- Alignment Reports
- Resume Optimization
- Development Plan
- Settings

Post-MVP navigation may add Applications, Interview Prep, and Organization workspaces.

## 3. First-Time User Flow

```text
Landing / Signup
  -> Onboarding
  -> Resume Upload
  -> Resume Review
  -> Capability Graph Generation
  -> Target Role Analysis
  -> First Alignment Report
  -> Resume Optimization
  -> Development Plan
  -> Workspace Home
```

### Step 1: Signup

User creates an account with email or OAuth.

The product asks for minimal initial information:

- Education or current role
- Target role family
- Experience level
- Preferred industries or companies
- Target location or constraints where relevant

### Step 2: Resume Upload

User provides a resume through:

- PDF upload
- Pasted resume text
- Manual profile entry when no resume is available

The UI should show upload status, extraction status, and privacy expectations.

### Step 3: Resume Intelligence Review

CareerLens extracts:

- Experiences
- Projects
- Education
- Skills
- Achievements
- Metrics and outcomes
- Evidence statements
- Missing or weak evidence

User reviews and edits extracted data before it becomes canonical profile context.

### Step 4: Talent Capability Graph

CareerLens generates:

- Capability map
- Capability categories
- Evidence links
- Confidence scores
- Strengths
- Skill and evidence gaps
- Missing information prompts

User can inspect which resume evidence supports each capability and mark capabilities as verified, developing, or aspirational.

### Step 5: Target Role Analysis

User provides a target role through:

- Job description paste
- Job description upload
- Curated role template
- Manual role entry

CareerLens generates Role Intelligence:

- Explicit requirements
- Hidden competency inferences
- Real job workflow explanation
- Evaluation signals
- Seniority expectations
- Evidence examples
- Requirement confidence

### Step 6: First Alignment Report

CareerLens compares the Talent Capability Graph with Role Intelligence and produces:

- Overall alignment score
- Capability-level alignment
- Requirement coverage
- Evidence-backed strengths
- Prioritized gaps
- Risks and assumptions
- Confidence indicators
- Recommended decision posture

The score should feel explainable and directional, not falsely precise.

### Step 7: Resume Optimization

CareerLens generates role-specific resume optimization suggestions:

- Capability coverage checklist
- Bullet improvement guidance
- Evidence placement suggestions
- Missing evidence warnings
- Low-value content to reduce or remove

The product must distinguish stronger communication of existing evidence from gaps that require new work.

### Step 8: Career Development Plan

CareerLens generates a gap-based plan:

- 2-week actions
- 1-month priorities
- 3-month capability plan
- Project recommendations
- Interview preparation focus
- Evidence-building actions

Each action links back to role requirements and alignment gaps.

## 4. Returning User Flow

```text
Open Home
  -> Review capability graph status, active target roles, and latest reports
  -> Update resume or profile evidence
  -> Analyze a new role
  -> Re-run alignment report
  -> Continue optimization or development plan
```

The home view should prioritize:

- Resume parsing and review status
- Capability graph completeness
- Active target roles
- Latest alignment reports
- Top gap themes
- Development plan progress
- Recent AI-generated insights that need review

## 5. Resume Intelligence Flow

```text
Resume Intelligence
  -> Upload or Paste Resume
  -> Extract Text
  -> Parse Sections
  -> Review Extracted Records
  -> Confirm Profile Updates
  -> Generate or Refresh Capability Graph
```

### Key Interactions

- Upload resume PDF
- Retry failed extraction
- Edit parsed sections
- Link evidence to projects or experiences
- Resolve duplicate skills or achievements
- Accept or reject AI-extracted records

### Resume Intelligence States

- No resume uploaded
- Uploading
- Extracting text
- Parsing resume
- Review required
- Ready for capability graph
- Extraction failed

## 6. Capability Graph Flow

```text
Capability Graph
  -> Overview
  -> Capability Categories
  -> Evidence Panel
  -> Confidence and Gaps
  -> Profile Versions
```

### Capability Graph Sections

- Technical capabilities
- Product and business capabilities
- Domain knowledge
- Communication and collaboration
- Leadership and execution
- Evidence quality
- Skill gaps

### Key Interactions

- Filter capabilities by role family
- Inspect supporting evidence
- Mark capability status
- Add missing evidence
- Compare graph versions
- Refresh analysis after profile changes

## 7. Role Intelligence Flow

```text
Role Intelligence
  -> Add Target Role
  -> Paste or Upload Job Description
  -> Extract Requirements
  -> Review Hidden Competencies
  -> Inspect Real Workflow
  -> Save Target Role
```

### Role Intelligence Sections

- Role overview
- Explicit requirements
- Hidden competency inferences
- Real job workflow
- Evaluation signals
- Required evidence examples
- Seniority expectations
- Confidence and assumptions

### Key Interactions

- Edit extracted requirements
- Adjust role family or seniority
- Compare with a curated role template
- Save target role for alignment
- Re-analyze role after JD changes

## 8. Alignment Report Flow

```text
Alignment Reports
  -> Select Capability Graph
  -> Select Target Role
  -> Generate Alignment Report
  -> Review Scores, Evidence, Strengths, and Gaps
  -> Continue to Resume Optimization or Development Plan
```

### Alignment Report Layout

The report should show:

- Overall alignment
- Dimension score breakdown
- Requirement coverage
- Evidence-backed strengths
- Prioritized gaps
- Risk and uncertainty indicators
- Confidence levels
- Recommended decision posture

### Alignment Dimensions

- Capability match
- Evidence strength
- Experience relevance
- Requirement coverage
- Gap severity
- Confidence

## 9. Resume Optimization Flow

```text
Resume Optimization
  -> Select Alignment Report
  -> Review Capability Coverage
  -> Inspect Suggestions
  -> Accept, Reject, or Revise Suggestions
  -> Export Guidance or Update Resume Draft
```

### Optimization Suggestion Types

- Evidence placement
- Bullet improvement
- Section gap
- Wording clarity
- Noise reduction
- Missing evidence warning

### Design Requirements

- Suggestions must reference target role requirements.
- Suggestions must reference existing candidate evidence when rewriting is possible.
- Suggestions must warn when the issue is a real capability or evidence gap.
- The product should not fabricate achievements.

## 10. Career Development Plan Flow

```text
Development Plan
  -> Select Alignment Report
  -> Generate Gap-Based Plan
  -> Review Milestones
  -> Save Actions
  -> Track Progress
  -> Refresh Plan After Capability Updates
```

### Plan Time Horizons

- Immediate: next 1-2 weeks
- Short term: next 1 month
- Medium term: next 3 months
- Strategic: next 6 months

### Plan Action Types

- Skill learning
- Project building
- Evidence creation
- Role workflow practice
- Interview preparation
- Company or domain research

## 11. AI Workspace Flow

The AI workspace may support open-ended interaction, but it must stay connected to structured product objects.

Examples:

- "Explain why my evidence strength is low for this role."
- "Which capabilities should I build before applying?"
- "What resume evidence supports my product thinking score?"
- "Turn this development plan into weekly milestones."

The AI should be able to reference:

- Resume versions
- Capability graphs
- Target roles
- Role requirements
- Alignment reports
- Resume optimization suggestions
- Development plans

The AI workspace should not replace the structured workflow.

## 12. Key UX States

### Empty States

Empty states should guide users toward concrete actions:

- Upload a resume
- Review extracted resume data
- Generate a capability graph
- Analyze a target role
- Generate an alignment report

### Loading States

AI workflows should show meaningful progress:

- Reading resume
- Extracting evidence
- Building capability graph
- Analyzing role requirements
- Comparing capabilities and requirements
- Generating explanations
- Saving structured report

### Error States

Errors should explain:

- What failed
- Whether user data was saved
- What the user can retry
- Whether AI analysis can continue with partial data

## 13. Design Tone

CareerLens should use concise, professional product language:

- "Resume Intelligence"
- "Capability Graph"
- "Role Intelligence"
- "Alignment Report"
- "Evidence"
- "Confidence"
- "Skill Gap"
- "Resume Optimization"
- "Development Plan"

Avoid:

- Fluffy AI phrases
- Over-personified assistant copy
- Chatbot-first labels
- Resume-writer-only language
- Black-box score language
