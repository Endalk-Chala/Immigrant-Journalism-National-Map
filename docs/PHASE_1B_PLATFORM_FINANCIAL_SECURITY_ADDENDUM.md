# Phase 1B Platform Monetization and Financial Security Addendum

This addendum is part of the Phase 1B Institutional Enrichment coding suite. It extends the revenue/funding and platform-infrastructure sections so that financial security is not reduced to annual revenue alone.

## Rationale

For immigrant-serving and community newsrooms, financial vulnerability may arise not only from small budgets but also from dependence on digital platforms, referral traffic, advertising systems, creator monetization programs, philanthropic grants, government advertising, or a small number of funders. Phase 1B should therefore record both **revenue sources** and **revenue dependence/concentration** where public evidence permits.

Public silence must not be interpreted as evidence that a revenue stream or monetization relationship does not exist.

---

# Platform monetization variables

## `platform_monetization_status`
Controlled values:
- `direct_platform_monetization_disclosed`
- `indirect_platform_revenue_disclosed`
- `multiple_platform_revenue_streams_disclosed`
- `no_platform_monetization_publicly_identified`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

`no_platform_monetization_publicly_identified` means relevant public sources were searched and no monetization relationship was identified; it does not prove the outlet has none.

## `monetized_platforms`
Semicolon-separated when explicit:
`youtube;facebook;instagram;tiktok;x;apple_news;google_news_or_discover;podcast_platforms;other`

## `platform_monetization_model`
Semicolon-separated where explicit:
- `ad_revenue_share`
- `creator_program_or_bonus`
- `video_monetization`
- `podcast_ad_revenue`
- `platform_subscription_or_membership`
- `platform_tipping_or_donations`
- `sponsored_content`
- `affiliate_or_commerce`
- `licensed_content_or_content_deal`
- `other`
- `unclear`

## `platform_revenue_dependency`
- `high_publicly_documented`
- `substantial_publicly_documented`
- `supplementary_publicly_documented`
- `minimal_publicly_documented`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

Do not infer this variable from follower counts alone.

## `platform_revenue_share_or_amount`
Numeric amount or percentage only when explicitly documented. Preserve year/time period.

## `platform_revenue_evidence_url`
Primary evidence URL.

---

# Referral and distribution dependence

## `referral_dependency_status`
- `search_central`
- `social_central`
- `search_and_social_central`
- `substantial_but_not_central`
- `owned_audience_dominant`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

## `major_referral_sources`
Semicolon-separated where documented:
`google_search;google_discover;facebook;instagram;tiktok;youtube;x;apple_news;news_aggregators;other`

## `owned_audience_channels`
Semicolon-separated:
`email_newsletter;sms;whatsapp;direct_web;mobile_app;print_distribution;radio_broadcast;television_broadcast;events;membership_database;other`

## `owned_audience_strength_public_signal`
- `strong`
- `moderate`
- `limited`
- `unclear`
- `not_searched`

This describes visible first-party audience infrastructure, not audience loyalty.

---

# Platform policy and algorithmic financial risk

## `platform_policy_financial_exposure`
Semicolon-separated when documented:
- `demonetization_risk`
- `account_suspension_or_termination_risk`
- `ad_suitability_restrictions`
- `algorithmic_visibility_reduction`
- `news_link_or_referral_reduction`
- `search_or_ai_zero_click_exposure`
- `copyright_claim_or_content_id_risk`
- `payment_program_change`
- `other`
- `none_documented_publicly`
- `unclear`

## `documented_demonetization_or_restriction_event`
- `yes`
- `no_event_found_publicly`
- `not_publicly_disclosed`
- `unclear`
- `not_searched`

If `yes`, document the event in the separate risk-event table rather than only in the organization row.

## `platform_risk_source_url`
Evidence URL.

---

# Revenue concentration and financial-security indicators

## `revenue_concentration_public_signal`
- `single_source_high_dependence`
- `few_sources_concentrated`
- `diversified_revenue_publicly_documented`
- `unclear`
- `not_publicly_disclosed`
- `not_searched`

## `grant_dependency_public_signal`
- `high`
- `substantial`
- `supplementary`
- `minimal`
- `unclear`
- `not_publicly_disclosed`
- `not_searched`

## `government_advertising_dependency_public_signal`
- `high`
- `substantial`
- `supplementary`
- `minimal`
- `unclear`
- `not_publicly_disclosed`
- `not_searched`

## `major_funding_loss_event_public`
- `yes`
- `no_event_found_publicly`
- `unclear`
- `not_searched`

If yes, record the event in the risk-event table.

## `financial_security_note`
Short descriptive field for publicly documented layoffs, closure threats, emergency fundraising, major grant expiration, platform-revenue shocks, or other financial conditions.

---

# Evidence rule

Platform presence is not the same as platform dependence, and platform dependence is not the same as platform monetization. These must remain separate variables.

Examples:
- An outlet may distribute heavily through WhatsApp but earn no platform revenue there.
- An outlet may earn YouTube ad revenue while still relying primarily on philanthropy.
- An outlet may depend on Facebook for referrals without receiving direct Facebook payments.
- A platform policy change can create financial exposure even where no direct monetization program exists because it can reduce traffic, advertising inventory, subscriptions, donations, or audience growth.

These variables should be incorporated into `data/phase1b/institutional_enrichment_v1.csv` before systematic enrichment begins.
