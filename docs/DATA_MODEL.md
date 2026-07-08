# CareerLens Data Model

## 1. Data Model Principles

CareerLens should store structured talent-role intelligence as first-class data. AI-generated analysis should be persisted as versioned, inspectable records connected to resume evidence, capability graph nodes, role requirements, and model metadata.

Core principles:

- Resume, profile, capability, role, report, optimization, and plan records are versionable.
- User-edited profile data is canonical.
- AI outputs reference source records and model versions.
- Capabilities and role requirements are normalized so they can be compared.
- Alignment scores are decomposed into dimensions with evidence and confidence.
- Resume optimization suggestions must link to real evidence or identified gaps.
- Application pipelines, LinkedIn integration, and real-time job scraping are post-MVP concerns.

## 2. User and Profile Entities

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
| target_seniority | text | student, intern, junior, mid |
| current_status | text | student, employed, searching |
| primary_role_family | text | AI Engineer, Software Engineer, etc. |
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
| analysis_json | jsonb | Capability and profile assessment |
| source | text | manual, resume_import, agent_analysis |
| created_at | timestamptz | Created timestamp |

## 3. Resume Intelligence Entities

## 3.1 resumes

Stores uploaded or pasted resume artifacts.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| profile_id | uuid | FK to career_profiles |
| title | text | Resume label |
| source_type | text | pdf_upload, text_paste, manual_import |
| raw_text | text | Extracted resume text |
| file_uri | text | Optional object storage path |
| parsing_status | text | pending, succeeded, failed |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 3.2 resume_versions

Stores versioned resume parses and optimization states.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| resume_id | uuid | FK to resumes |
| version_number | integer | Incrementing version |
| raw_text_hash | text | Change detection |
| parsed_json | jsonb | Extracted structured fields |
| model_metadata_json | jsonb | Model and prompt metadata |
| created_at | timestamptz | Created timestamp |

## 3.3 resume_sections

Stores parsed sections from a resume version.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| resume_version_id | uuid | FK to resume_versions |
| section_type | text | summary, experience, project, education, skills, awards |
| heading | text | Original section heading |
| content | text | Section text |
| order_index | integer | Resume order |
| confidence | numeric | Extraction confidence |
| created_at | timestamptz | Created timestamp |

## 3.4 resume_evidence

Stores atomic evidence extracted from resumes and linked to capabilities or requirements.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| resume_version_id | uuid | FK to resume_versions |
| section_id | uuid | Nullable FK to resume_sections |
| evidence_type | text | achievement, responsibility, technology, metric, credential |
| text | text | Evidence excerpt or normalized statement |
| normalized_json | jsonb | Structured evidence details |
| confidence | numeric | Extraction confidence |
| created_at | timestamptz | Created timestamp |

## 4. Profile Detail Entities

## 4.1 experiences

Stores work, internship, research, and leadership experience.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| profile_id | uuid | FK to career_profiles |
| source_resume_evidence_id | uuid | Nullable FK to resume_evidence |
| organization | text | Company, lab, or team |
| title | text | Role title |
| experience_type | text | internship, full_time, research, campus |
| start_date | date | Nullable |
| end_date | date | Nullable |
| description | text | User-editable description |
| achievements_json | jsonb | Structured achievements |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 4.2 projects

Stores user projects as evidence for capabilities.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| profile_id | uuid | FK to career_profiles |
| source_resume_evidence_id | uuid | Nullable FK to resume_evidence |
| name | text | Project name |
| description | text | Project summary |
| role | text | User's role |
| tech_stack | text[] | Technologies used |
| outcome | text | Impact or result |
| link | text | GitHub, demo, paper, portfolio |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 4.3 education_records

Stores education records and credentials.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| profile_id | uuid | FK to career_profiles |
| institution | text | School or program |
| degree | text | Degree or credential |
| field_of_study | text | Major or specialization |
| start_date | date | Nullable |
| end_date | date | Nullable |
| evidence_json | jsonb | Courses, awards, GPA, certificates |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 4.4 skills

Stores normalized skills.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| name | text | Skill name |
| category | text | programming, AI, product, domain, communication |
| normalized_name | text | Deduplication key |
| created_at | timestamptz | Created timestamp |

## 4.5 profile_skills

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

## 4.6 career_preferences

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

## 5. Capability Intelligence Entities

## 5.1 capability_graphs

Stores versioned Talent Capability Graphs.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| profile_id | uuid | FK to career_profiles |
| profile_version_id | uuid | FK to profile_versions |
| graph_version | integer | Incrementing graph version |
| summary | text | Capability graph summary |
| completeness_score | numeric | Evidence coverage |
| model_metadata_json | jsonb | Model and prompt metadata |
| created_at | timestamptz | Created timestamp |

## 5.2 capabilities

Stores normalized capability nodes.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| graph_id | uuid | FK to capability_graphs |
| name | text | Capability name |
| category | text | technical, product, domain, collaboration, leadership |
| level | text | emerging, working, strong, advanced |
| confidence | numeric | Confidence in inferred capability |
| rationale | text | Why this capability was inferred |
| status | text | verified, developing, aspirational |
| created_at | timestamptz | Created timestamp |

## 5.3 capability_evidence

Links capabilities to supporting evidence.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| capability_id | uuid | FK to capabilities |
| source_type | text | resume_evidence, experience, project, education, profile_skill |
| source_id | uuid | Source record ID |
| evidence_strength | text | weak, moderate, strong |
| confidence | numeric | Link confidence |
| notes | text | Evidence rationale |
| created_at | timestamptz | Created timestamp |

## 5.4 capability_gaps

Stores known or inferred capability gaps.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| graph_id | uuid | FK to capability_graphs |
| capability_name | text | Gap area |
| category | text | technical, product, domain, collaboration, leadership |
| severity | text | low, medium, high |
| evidence_need | text | What evidence would reduce the gap |
| confidence | numeric | Gap confidence |
| created_at | timestamptz | Created timestamp |

## 6. Role Intelligence Entities

## 6.1 role_templates

Stores reusable role expectations.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| role_name | text | Example: AI Product Manager |
| role_family | text | AI, software, product, data |
| seniority | text | intern, junior, mid |
| required_capabilities | text[] | Expected capabilities |
| preferred_capabilities | text[] | Nice-to-have capabilities |
| responsibilities | text[] | Common responsibilities |
| evaluation_signals | text[] | What hiring teams value |
| workflow_json | jsonb | Real job workflow explanation |
| evidence_examples_json | jsonb | Artifacts that demonstrate fit |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 6.2 target_roles

Stores user-created target roles or job descriptions for analysis.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| role_template_id | uuid | Nullable FK to role_templates |
| title | text | Role title |
| company_name | text | Optional company name |
| role_family | text | AI, software, product, data |
| seniority | text | intern, junior, mid |
| location | text | Optional |
| source_url | text | Optional |
| jd_text | text | Original job description |
| analysis_status | text | pending, succeeded, failed |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 6.3 role_requirements

Stores normalized explicit and inferred role requirements.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| target_role_id | uuid | FK to target_roles |
| requirement_type | text | explicit, hidden_inference, preferred |
| capability_name | text | Normalized capability |
| category | text | technical, product, domain, collaboration, leadership |
| importance | text | low, medium, high, critical |
| evidence_expectation | text | Evidence that would demonstrate readiness |
| source_text | text | JD excerpt or inference note |
| rationale | text | Requirement explanation |
| confidence | numeric | Requirement confidence |
| created_at | timestamptz | Created timestamp |

## 6.4 role_workflows

Stores real job workflow explanations.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| target_role_id | uuid | FK to target_roles |
| workflow_summary | text | What the role likely does day to day |
| responsibility_map_json | jsonb | Responsibilities mapped to capabilities |
| collaboration_context_json | jsonb | Teams, stakeholders, handoffs |
| evaluation_signals_json | jsonb | Signals used in hiring or performance |
| confidence | numeric | Workflow confidence |
| created_at | timestamptz | Created timestamp |

## 7. Alignment Entities

## 7.1 alignment_reports

Stores explainable Talent-Role Alignment Reports.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| profile_id | uuid | FK to career_profiles |
| capability_graph_id | uuid | FK to capability_graphs |
| target_role_id | uuid | FK to target_roles |
| overall_score | numeric | 0-100 directional score |
| confidence_level | text | low, medium, high |
| recommendation | text | strong_fit, possible_fit, prepare_first, low_fit |
| summary | text | Human-readable result |
| score_breakdown_json | jsonb | Dimension scores |
| strengths_json | jsonb | Evidence-backed strengths |
| gaps_json | jsonb | Capability and evidence gaps |
| risks_json | jsonb | Important uncertainties or mismatch risks |
| evidence_json | jsonb | Source references supporting the analysis |
| assumptions_json | jsonb | Agent assumptions |
| model_metadata_json | jsonb | Model, prompt, token metadata |
| created_at | timestamptz | Created timestamp |

### score_breakdown_json Example

```json
{
  "capability_match": 76,
  "evidence_strength": 68,
  "experience_relevance": 72,
  "requirement_coverage": 64,
  "gap_severity": 58,
  "confidence": 70
}
```

## 7.2 alignment_requirement_results

Stores requirement-level alignment decisions.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| report_id | uuid | FK to alignment_reports |
| role_requirement_id | uuid | FK to role_requirements |
| status | text | met, partially_met, missing, unclear |
| matched_capability_ids | uuid[] | Related capabilities |
| evidence_json | jsonb | Supporting or missing evidence |
| gap_severity | text | low, medium, high |
| confidence | numeric | Match confidence |
| explanation | text | Requirement-level rationale |
| created_at | timestamptz | Created timestamp |

## 8. Resume Optimization Entities

## 8.1 resume_optimizations

Stores optimization sessions generated from an alignment report.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| resume_version_id | uuid | FK to resume_versions |
| target_role_id | uuid | FK to target_roles |
| alignment_report_id | uuid | FK to alignment_reports |
| summary | text | Optimization overview |
| model_metadata_json | jsonb | Model and prompt metadata |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 8.2 resume_optimization_suggestions

Stores specific target-role resume suggestions.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| optimization_id | uuid | FK to resume_optimizations |
| suggestion_type | text | evidence_placement, bullet_rewrite, section_gap, wording, remove_noise |
| target_section_id | uuid | Nullable FK to resume_sections |
| related_requirement_id | uuid | Nullable FK to role_requirements |
| related_evidence_id | uuid | Nullable FK to resume_evidence |
| title | text | Suggestion title |
| rationale | text | Why the suggestion matters |
| suggested_text | text | Optional suggested wording |
| priority | integer | Lower number means higher priority |
| status | text | proposed, accepted, rejected, revised |
| confidence | numeric | Suggestion confidence |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 9. Career Development Plan Entities

## 9.1 development_plans

Stores generated Career Development Plans.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | FK to users |
| profile_id | uuid | FK to career_profiles |
| capability_graph_id | uuid | FK to capability_graphs |
| target_role_id | uuid | FK to target_roles |
| alignment_report_id | uuid | FK to alignment_reports |
| title | text | Plan title |
| summary | text | Plan overview |
| model_metadata_json | jsonb | Model and prompt metadata |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 9.2 development_actions

Stores plan milestones and preparation actions.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| plan_id | uuid | FK to development_plans |
| action_type | text | skill, project, interview, evidence, research |
| title | text | Action title |
| description | text | Action details |
| horizon | text | 2_weeks, 1_month, 3_months, 6_months |
| priority | integer | Lower number means higher priority |
| effort_level | text | low, medium, high |
| status | text | todo, in_progress, done |
| linked_gap_json | jsonb | Alignment gaps and requirements addressed |
| success_evidence | text | What completion should produce |
| created_at | timestamptz | Created timestamp |
| updated_at | timestamptz | Updated timestamp |

## 10. AI Operations Entities

## 10.1 agent_runs

Tracks AI workflow execution.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| user_id | uuid | Nullable for system jobs |
| agent_type | text | resume, capability_graph, role_intelligence, alignment, resume_optimization, development_plan |
| status | text | queued, running, succeeded, failed |
| input_refs_json | jsonb | Source record references |
| output_refs_json | jsonb | Generated record references |
| error_message | text | Failure reason |
| model_metadata_json | jsonb | Model and prompt metadata |
| started_at | timestamptz | Start time |
| completed_at | timestamptz | End time |

## 10.2 embeddings

Tracks vectorized content references.

| Field | Type | Notes |
| --- | --- | --- |
| id | uuid | Primary key |
| source_type | text | resume_evidence, capability, role_requirement, alignment_report, role_template |
| source_id | uuid | Source record ID |
| chunk_index | integer | Chunk order |
| content_hash | text | Detect changes |
| vector_store_id | text | External vector ID |
| metadata_json | jsonb | Search metadata |
| created_at | timestamptz | Created timestamp |

## 11. Post-MVP Entities

Application pipeline and workspace note entities are intentionally excluded from the V2 MVP. Future modules may include:

- applications
- application_status_events
- workspace_notes
- interview_preparation_records
- organization_accounts

## 12. Relationship Summary

```text
users
  -> career_profiles
  -> profile_versions
  -> resumes -> resume_versions -> resume_sections
  -> resume_evidence
  -> experiences
  -> projects
  -> education_records
  -> profile_skills -> skills
  -> career_preferences

career_profiles
  -> capability_graphs -> capabilities -> capability_evidence
  -> capability_gaps

users
  -> target_roles -> role_requirements
  -> role_workflows

capability_graphs + target_roles
  -> alignment_reports -> alignment_requirement_results
  -> resume_optimizations -> resume_optimization_suggestions
  -> development_plans -> development_actions

agent_runs
  -> generated resume_versions, capability_graphs, target_roles, alignment_reports,
     resume_optimizations, and development_plans
```

## 13. MVP Migration Order

Recommended initial migration order:

1. users
2. career_profiles
3. resumes
4. resume_versions
5. resume_sections
6. resume_evidence
7. experiences
8. projects
9. education_records
10. skills
11. profile_skills
12. career_preferences
13. capability_graphs
14. capabilities
15. capability_evidence
16. capability_gaps
17. role_templates
18. target_roles
19. role_requirements
20. role_workflows
21. alignment_reports
22. alignment_requirement_results
23. resume_optimizations
24. resume_optimization_suggestions
25. development_plans
26. development_actions
27. agent_runs
28. embeddings

Post-MVP migrations:

- applications
- workspace_notes
- organization_accounts
