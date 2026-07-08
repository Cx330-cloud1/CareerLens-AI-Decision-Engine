CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS users (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  email text NOT NULL UNIQUE,
  password_hash text,
  display_name text,
  locale text NOT NULL DEFAULT 'en-US',
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS talent_profiles (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id uuid NOT NULL REFERENCES users(id),
  headline text,
  summary text,
  target_seniority text,
  current_status text,
  primary_path text,
  completeness_score numeric NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS companies (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name text NOT NULL,
  slug text NOT NULL UNIQUE,
  headquarters text,
  industry text,
  company_stage text,
  business_model text,
  ai_strategy text,
  product_areas text[] NOT NULL DEFAULT '{}',
  technical_focus text[] NOT NULL DEFAULT '{}',
  hiring_preferences_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  company_dna_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  source_notes_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  last_reviewed_at timestamptz,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS roles (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  role_name text NOT NULL,
  role_family text NOT NULL,
  seniority text,
  required_skills text[] NOT NULL DEFAULT '{}',
  preferred_skills text[] NOT NULL DEFAULT '{}',
  responsibilities text[] NOT NULL DEFAULT '{}',
  evaluation_signals text[] NOT NULL DEFAULT '{}',
  evidence_examples_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  interview_focus_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS match_reports (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id uuid NOT NULL REFERENCES users(id),
  profile_id uuid NOT NULL REFERENCES talent_profiles(id),
  company_id uuid REFERENCES companies(id),
  role_id uuid REFERENCES roles(id),
  overall_score numeric NOT NULL,
  confidence_level text NOT NULL,
  recommendation text NOT NULL,
  summary text,
  score_breakdown_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  strengths_json jsonb NOT NULL DEFAULT '[]'::jsonb,
  gaps_json jsonb NOT NULL DEFAULT '[]'::jsonb,
  evidence_json jsonb NOT NULL DEFAULT '[]'::jsonb,
  assumptions_json jsonb NOT NULL DEFAULT '[]'::jsonb,
  model_metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS career_plans (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id uuid NOT NULL REFERENCES users(id),
  profile_id uuid NOT NULL REFERENCES talent_profiles(id),
  match_report_id uuid REFERENCES match_reports(id),
  title text NOT NULL,
  summary text,
  plan_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  model_metadata_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS knowledge_sources (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  source_type text NOT NULL,
  title text NOT NULL,
  uri text,
  source_notes_json jsonb NOT NULL DEFAULT '{}'::jsonb,
  freshness_label text,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
