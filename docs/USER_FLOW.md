# CareerLens User Flow

## 1. Product Experience Model

CareerLens should feel like a structured career intelligence workspace. The user should not land in an empty chat window. The primary experience is a workspace with persistent profile, market intelligence, opportunity analysis, roadmap, and application pipeline.

## 2. Primary Navigation

Recommended main navigation:

- Home
- Career Profile
- Market Intelligence
- Opportunities
- Strategy Roadmap
- Applications
- AI Workspace
- Settings

## 3. First-Time User Flow

```text
Landing / Signup
  -> Onboarding
  -> Profile Input
  -> Career Profile Analysis
  -> Target Path Selection
  -> First Opportunity Match
  -> Strategy Roadmap
  -> Workspace Home
```

### Step 1: Signup

User creates an account with email or OAuth.

The product asks for minimal initial information:

- Education or current role
- Target career path
- Experience level
- Preferred industries

### Step 2: Profile Input

User can provide:

- Resume text or file
- LinkedIn-style profile information
- Projects
- Skills
- Career preferences

The UI should support both upload and manual editing.

### Step 3: Profile Analysis

CareerLens generates:

- Professional identity summary
- Capability map
- Strengths
- Weaknesses
- Suitable career directions
- Missing information prompts

User reviews and edits the profile before using it for matching.

### Step 4: Target Path Selection

User selects one or more career paths:

- AI Engineer
- Software Engineer
- AI Product Manager
- AI Solution Engineer
- Data roles
- Other technology role

CareerLens adapts scoring and roadmap logic based on the selected path.

### Step 5: First Opportunity Match

User chooses a company or creates an opportunity.

CareerLens produces:

- Match score
- Score breakdown
- Evidence
- Strengths
- Skill gaps
- Application recommendation

### Step 6: Strategy Roadmap

CareerLens generates a roadmap:

- 2-week actions
- 1-month actions
- 3-month skill plan
- Project recommendations
- Application strategy

User can save roadmap items as tasks.

## 4. Returning User Flow

```text
Open Home
  -> Review profile status, active opportunities, roadmap progress
  -> Continue application preparation
  -> Update profile or target path
  -> Re-run match reports
```

The home view should prioritize:

- Profile completeness
- Active target opportunities
- Top skill gaps
- Roadmap progress
- Upcoming preparation tasks
- Recent AI insights

## 5. Career Profile Flow

```text
Career Profile
  -> Profile Overview
  -> Capability Map
  -> Experience and Projects
  -> Skills
  -> Preferences
  -> Profile Versions
```

### Key Interactions

- Edit profile sections
- Re-run profile analysis
- Compare profile versions
- Mark skills as verified, developing, or aspirational
- Add evidence to skills through projects or experience

## 6. Market Intelligence Flow

```text
Market Intelligence
  -> Search Company or Industry
  -> Open Intelligence Page
  -> Save Company
  -> Compare With Profile
  -> Create Opportunity
```

### Company Page Sections

- Overview
- Business model
- AI strategy
- Product areas
- Technical focus
- Hiring signals
- Relevant roles
- Fit with current profile

### Industry Page Sections

- Emerging roles
- Skill trends
- Technology changes
- Hiring market notes
- Suggested preparation areas

## 7. Opportunity Matching Flow

```text
Opportunities
  -> Create or Import Opportunity
  -> Select Company and Role
  -> Review Requirements
  -> Generate Match Report
  -> Save to Application Pipeline
```

### Match Report Layout

The report should show:

- Overall match score
- Score breakdown
- Evidence by category
- Strengths
- Gaps
- Risks
- Recommended action

The score should feel explainable and directional, not falsely precise.

## 8. Strategy Roadmap Flow

```text
Strategy Roadmap
  -> Select target role or opportunity
  -> Generate roadmap
  -> Review milestones
  -> Save tasks
  -> Track progress
```

### Roadmap Time Horizons

- Immediate: next 1-2 weeks
- Short term: next 1 month
- Medium term: next 3 months
- Strategic: next 6-12 months

### Roadmap Item Types

- Skill learning
- Project building
- Resume improvement
- Company research
- Interview preparation
- Networking action

## 9. Application Intelligence Flow

```text
Applications
  -> Pipeline Board
  -> Opportunity Detail
  -> Preparation Checklist
  -> Resume Version
  -> Interview Prep
  -> Outcome Notes
```

### Application Statuses

- Researching
- Preparing
- Applied
- Interviewing
- Offer
- Rejected
- Archived

### Application Detail Should Include

- Role and company
- Match report
- Resume version
- Preparation tasks
- Notes
- Interview questions
- Follow-up reminders

## 10. AI Workspace Flow

The AI workspace should support open-ended interaction, but it must stay connected to structured product objects.

Examples:

- "Compare my profile with ByteDance AI Product Manager roles."
- "What projects would improve my AI Engineer profile?"
- "Explain why my domain alignment score is low."
- "Turn this roadmap recommendation into weekly tasks."

The AI should be able to reference:

- Profile
- Companies
- Opportunities
- Match reports
- Roadmaps
- Application notes

## 11. Key UX States

### Empty States

Empty states should guide users toward concrete actions:

- Add profile information
- Analyze profile
- Save a company
- Create opportunity
- Generate match report

### Loading States

AI workflows should show meaningful progress:

- Reading profile
- Retrieving company intelligence
- Comparing requirements
- Generating explanation
- Saving report

### Error States

Errors should explain:

- What failed
- Whether user data was saved
- What the user can retry

## 12. Design Tone

CareerLens should use concise, professional product language:

- "Career Profile"
- "Market Intelligence"
- "Match Report"
- "Skill Gap"
- "Roadmap"
- "Application Pipeline"

Avoid fluffy AI phrases and over-personified assistant copy.
