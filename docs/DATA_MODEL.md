# CareerLens Data Model

## 1. Data Model Principles

CareerLens should store structured career intelligence as first-class data. AI-generated text should be persisted as versioned, inspectable records connected to source objects.

Core principles:

- User profile data is canonical and editable.
- AI outputs reference source records and model versions.
- Match scores are decomposed into dimensions.
- Company and market intelligence are reusable platform data.
- Company-role targets connect talent profiles, role intelligence, company DNA, match reports, and action plans.
- Application pipelines, workspace notes, LinkedIn integration, and real-time job scraping are post-MVP concerns.

## 2. Core Entities

## 2.1 users

Stores account-level user information.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| email | text | Unique |
| password_hash | text | Nullable if OAuth-only |
| display_name | text | User-facing name |
| locale | text | Example: zh-CN, en-US |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 2.2 career_profiles

Stores the current canonical career profile for a user.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| headline | text | Professional headline |
| summary | text | Structured professional summary |
| target_seniority | text | Student, intern, junior, mid-level |
| current_status | text | Student, employed, searching |
| primary_path | text | AI Engineer, Software Engineer, etc. |
| completeness_score | numeric | Profile completeness |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 2.3 profile_versions

Stores snapshots of profile state and AI analysis over time.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| profile_id | uuid | FK to career_profiles |
| version_number | integer | Incrementing version |
| snapshot_json | jsonb | Profile snapshot |
| analysis_json | jsonb | Capability assessment |
| source | text | manual, resume_import, agent_analysis |
| created_at | timestamptz | Created timestamp |

## 2.4 resumes

Stores uploaded or pasted resume artifacts.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| profile_id | uuid | FK to career_profiles |
| title | text | Resume label |
| raw_text | text | Extracted resume text |
| file_uri | text | Optional object storage path |
| parsed_json | jsonb | Extracted structured fields |
| created_at | timestamptz | Created timestamp |

## 2.5 experiences

Stores work, internship, research, and leadership experience.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| profile_id | uuid | FK to career_profiles |
| organization | text | Company, lab, or team |
| title | text | Role title |
| experience_type | text | internship, full_time, research, campus |
| start_date | date | Nullable |
| end_date | date | Nullable |
| description | text | User-editable description |
| achievements_json | jsonb | Structured achievements |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 2.6 projects

Stores user projects as evidence for capabilities.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| profile_id | uuid | FK to career_profiles |
| name | text | Project name |
| description | text | Project summary |
| role | text | User's role |
| tech_stack | text[] | Technologies used |
| outcome | text | Impact or result |
| link | text | GitHub, demo, paper, portfolio |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 2.7 skills

Stores normalized skills.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| name | text | Skill name |
| category | text | programming, AI, product, domain, communication |
| normalized_name | text | Deduplication key |
| created_at | timestamptz | Created timestamp |

## 2.8 profile_skills

Connects skills to user profiles.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| profile_id | uuid | FK to career_profiles |
| skill_id | uuid | FK to skills |
| proficiency | text | beginner, intermediate, advanced |
| confidence | numeric | AI or user confidence |
| evidence_json | jsonb | Linked projects, experiences, resumes |
| status | text | verified, developing, aspirational |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 2.9 career_preferences

Stores career preference signals.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| profile_id | uuid | FK to career_profiles |
| preferred_roles | text[] | Target roles |
| preferred_industries | text[] | Target industries |
| preferred_locations | text[] | Cities or remote |
| company_stage_preference | text | startup, large tech, enterprise |
| work_style_preferences | jsonb | Structured preference data |
| constraints_json | jsonb | Visa, location, timing, etc. |
| updated_at | timestamptz | Updated timestamp |

## 3. Market Intelligence Entities

## 3.1 companies

Stores company intelligence records.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| name | text | Company name |
| slug | text | Unique URL key |
| headquarters | text | Optional |
| industry | text | Primary industry |
| company_stage | text | large_tech, startup, enterprise |
| business_model | text | Structured summary |
| ai_strategy | text | AI strategy summary |
| product_areas | text[] | Major products |
| technical_focus | text[] | Technical domains |
| hiring_preferences_json | jsonb | Candidate signals |
| company_dna_json | jsonb | Talent needs, working style signals, strategic priorities |
| source_notes_json | jsonb | Source metadata |
| last_reviewed_at | timestamptz | Freshness tracking |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 3.2 industry_insights

Stores reusable industry and role trend intelligence.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| title | text | Insight title |
| industry | text | Industry category |
| role_family | text | AI, software, product, data |
| summary | text | Human-readable insight |
| skill_trends | text[] | Relevant skills |
| source_notes_json | jsonb | Source metadata |
| valid_from | date | Start date |
| valid_to | date | Optional |
| created_at | timestamptz | Created timestamp |

## 3.3 role_templates

Stores reusable role expectations.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| role_name | text | Example: AI Product Manager |
| role_family | text | AI, software, product, data |
| seniority | text | intern, junior, mid |
| required_skills | text[] | Expected skills |
| preferred_skills | text[] | Nice-to-have skills |
| responsibilities | text[] | Common responsibilities |
| evaluation_signals | text[] | What hiring teams value |
| evidence_examples_json | jsonb | Projects, experiences, or artifacts that demonstrate fit |
| interview_focus_json | jsonb | Likely interview and preparation areas |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 4. Target and Matching Entities

## 4.1 company_role_targets

Stores user-created company-role targets for decision analysis. These are not application pipeline records.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| company_id | uuid | Nullable FK to companies |
| role_template_id | uuid | Nullable FK to role_templates |
| title | text | Role title |
| role_family | text | AI, software, product, data |
| seniority | text | intern, junior, mid |
| location | text | Optional |
| source_url | text | Optional |
| description | text | Optional manually entered role description |
| requirements_json | jsonb | Normalized requirements |
| status | text | active, archived |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 4.2 match_reports

Stores explainable company-role target matching results.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| profile_id | uuid | FK to career_profiles |
| profile_version_id | uuid | FK to profile_versions |
| target_id | uuid | FK to company_role_targets |
| overall_score | numeric | 0-100 directional score |
| confidence_level | text | low, medium, high |
| recommendation | text | pursue_now, prepare_first, deprioritize |
| summary | text | Human-readable result |
| score_breakdown_json | jsonb | Dimension scores |
| strengths_json | jsonb | Evidence-backed strengths |
| gaps_json | jsonb | Skill and experience gaps |
| evidence_json | jsonb | Source references supporting the analysis |
| assumptions_json | jsonb | Agent assumptions |
| model_metadata_json | jsonb | Model, prompt, token metadata |
| created_at | timestamptz | Created timestamp |

### score_breakdown_json Example

```json
{
  "skill_alignment": 76,
  "experience_relevance": 68,
  "domain_alignment": 55,
  "career_preference_alignment": 82,
  "evidence_strength": 64,
  "confidence": 70
}
```

## 5. Career Action Plan Entities

## 5.1 action_plans

Stores generated career action plans.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| profile_id | uuid | FK to career_profiles |
| target_role | text | Action plan target |
| target_id | uuid | Nullable FK to company_role_targets |
| title | text | Action plan title |
| summary | text | Action plan overview |
| created_from_match_report_id | uuid | Nullable FK |
| model_metadata_json | jsonb | Model and prompt metadata |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 5.2 action_items

Stores action plan milestones and preparation actions.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| action_plan_id | uuid | FK to action_plans |
| item_type | text | skill, project, interview, research |
| title | text | Item title |
| description | text | Item details |
| horizon | text | 2_weeks, 1_month, 3_months, 6_months |
| priority | integer | Lower number means higher priority |
| status | text | todo, in_progress, done |
| evidence_json | jsonb | Match gaps and source evidence behind this action |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 5.3 Post-MVP applications

Stores application pipeline records after the MVP. This table is intentionally excluded from the first version.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| target_id | uuid | FK to company_role_targets |
| match_report_id | uuid | Nullable FK |
| status | text | researching, preparing, applied, interviewing, offer, rejected, archived |
| current_resume_id | uuid | Nullable FK to resumes |
| notes | text | User notes |
| next_action | text | Next action |
| next_action_due_at | timestamptz | Optional |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 5.4 Post-MVP workspace_notes

Stores Notion-style notes and saved insights after the MVP. This table is intentionally excluded from the first version.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| title | text | Note title |
| body | text | Markdown or rich text payload |
| linked_entity_type | text | company, target, action_plan, application |
| linked_entity_id | uuid | Optional polymorphic reference |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 6. AI Operations Entities

## 6.1 agent_runs

Tracks AI workflow execution.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | Nullable for system jobs |
| agent_type | text | profile, company_dna, role_intelligence, matching, action_plan |
| status | text | queued, running, succeeded, failed |
| input_refs_json | jsonb | Source record references |
| output_refs_json | jsonb | Generated record references |
| error_message | text | Failure reason |
| model_metadata_json | jsonb | Model and prompt metadata |
| started_at | timestamptz | Start time |
| completed_at | timestamptz | End time |

## 6.2 embeddings

Tracks vectorized content references.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| source_type | text | resume, company, role_template, target, match_report |
| source_id | uuid | Source record ID |
| chunk_index | integer | Chunk order |
| content_hash | text | Detect changes |
| vector_store_id | text | External vector ID |
| metadata_json | jsonb | Search metadata |
| created_at | timestamptz | Created timestamp |

## 7. Relationship Summary

```text
users
  -> career_profiles
  -> profile_versions
  -> experiences
  -> projects
  -> profile_skills -> skills
  -> career_preferences

users
  -> company_role_targets -> companies
  -> company_role_targets -> role_templates
  -> match_reports
  -> action_plans -> action_items

companies
  -> company_role_targets

agent_runs
  -> generated profile_versions, match_reports, action_plans, company DNA, role intelligence
```

## 8. MVP Migration Order

Recommended initial migration order:

1. users
2. career_profiles
3. resumes
4. experiences
5. projects
6. skills
7. profile_skills
8. career_preferences
9. companies
10. role_templates
11. company_role_targets
12. match_reports
13. action_plans
14. action_items
15. agent_runs
16. embeddings

Post-MVP migrations:

- applications
- workspace_notes
