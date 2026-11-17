# Queue

New papers bearing on a seed locus (`docs/longevitymap_v2/data/seed_variants.csv`), for the
curator. Each entry: the locus, one line on why, the passage that says it (verbatim, with where and when it was
read), and every identifier the paper has. The curator takes it from here; the scout never tiers a row. An entry the curator has taken says so in a **Taken** line naming its row, or a **Closed** line saying why no row follows.

## Open

The backfill 2015-01-01 → 2026-10-20 (2026-11-17): two entries for loci outside every seed (the lead's rule a), then one entry per row for papers no row cites (rule b), at abstract depth; each quote is the abstract's sentence as PubMed holds it, read 2026-11-17.

### GWAS Catalog — genome-wide lines for lifespan, longevity, healthspan or death at no seed or row locus (thirteen lines, eight studies)

- **Why:** the lead's rule (a) asks for every locus genome-wide for lifespan, longevity, healthspan or age at death that is not a seed locus. The Catalog's associations at P ≤ 5e-8 under the four terms (EFO_0007796, OBA_VT0005372, EFO_0009762, EFO_0005056), plus Lunetta 2007's morbidity-free survival study (GCST000103, mapped outside the four), were compared by position (GRCh38) with every seed variant and every row's stated position: 181 lines; 149 at a seed or row rsID, 15 within 500 kb of a seed, 6 without a chromosome. The six chromosome-less lines are five of Wright 2019's `im:` lines and Pilling 2017's chr13 line. The five Wright lines give numbers that fall at seeds 80 (CHRNB4), 57 (CDKN2B-AS1) and 46 (LPA) if read as positions on 15, 9 and 6. The chromosome is inferred from the number alone and is not checked. Pilling 2017's line is listed below. The lines below sit 2 Mb or more from the nearest seed. Most come from small or early scans, and none is in a row. The curator, or the lead, decides whether any is a row.
- **Found by:** the backfill (2026-11-17), Catalog REST v2 (`/studies?efo_id=`, `/associations?accession_id=`), read 2026-11-17.
- **Lines in no track** (no track's CSV, seed or row names them):
  - rs17685 (POR, 7:75,986,787), father's age at death, P 5e-8, Wright 2019 (PMID 31484785, GCST009447, 309,383 Europeans).
  - rs4709783 (C6orf118, 6:163,874,119), mother's age at death, P 5e-8, Pilling 2016 (PMID 27015805, GCST003393, 52,776); 3.1 Mb from seed 46's nearest variant.
  - chr13:31,871,514 (no rsID given), mother's attained age, P 5e-8, Pilling 2017 (PMID 29227965, GCST006696, 412,937); 1.18 Mb from KL-VS (row 73).
  - rs78441534 (MYO5B, 18:50,083,001), longevity 100+, P 5e-8, PMID 33948810 (GCST012419, 1,320 cases, 2,899 controls), a paper rows already cite for other loci.
  - rs32566 (ICE1, 5:5,792,394) and rs1412337 (DPT/XCL1, 1:168,649,403), morbidity-free survival, P 2e-9 each, Lunetta 2007 (PMID 17903295, GCST000103, 558 Framingham participants, the 100K chip). This corrects the Track B verdict of 2026-11-17, which read only the four terms and missed GCST000103.
- **Lines the tracks listed but no seed took** (`B_gwascatalog_gw_leads.csv`, in_v1 "no"):
  - rs4426183 (MYL2, 12:110,935,600), combined parental attained age, P 2e-11, Pilling 2017 (GCST006697); 511 kb from row 71's rs3184504 (SH2B3), so possibly row 71's locus.
  - rs10198124 (2:35,216,373), parental lifespan, P 2e-8, Joshi 2017 (PMID 29030599, GCST004983).
  - Yashin 2015 (PMID 25918517, GCST002846, 679 women), lifespan: rs12949468 (TLK2) 5e-20, rs7894051 (ECHS1) 3e-10, rs4904670 (NRDE2) 2e-9, rs2292664 (RIMBP2) 1e-8, rs2229188 (CYP51A1) 2e-8.
- **Not a lifespan line:** rs10496265 (17903295, GCST000096) at 1e-8 is age at menopause, mapped under EFO_0005056.
- **Unknown:** whether each line survived in its paper's own replication, and whether the tracks set any aside on purpose; B's synthesis names none of them.

### pmid-30299504 — rs1927465 (between CYP26A1 and MYOF, 10q23.33): a new longevity association in the Long Life Family Study, not a seed locus

- **Why:** A GWAS of longevity in the LLFS families reports a "strong new association" at rs1927465, outside every seed locus and every row, confirmed in the Health and Retirement Study. Whether it reached genome-wide significance, and its effect allele and size, are not in the abstract. If it did, this is a candidate new row under the lead's rule (a).
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Yashin AI et al., "Genetics of Human Longevity From Incomplete Data: New Findings From the Long Life Family Study." *The journals of gerontology. Series A, Biological sciences and medical sciences*, 2018 Oct 8. PMID 30299504, doi 10.1093/gerona/gly057. GWAS of exceptional lifespans in families, missing lifespans predicted; replication in HRS.
    > In addition to detection of strong associations of SNPs in APOE, TOMM40, NECTIN2, and APOC1 genes with longevity, we also detected a strong new association with longevity of rs1927465, located between the CYP26A1 and MYOF genes on chromosome 10.
- **Unknown:** the P value of rs1927465 in discovery and in HRS, its effect allele and frequency, and whether the full text or its supplement gives them. Is the full text open? Not checked. Whether rs1927465 has a proxy in Deelen 2019, Timmers 2019 or Pilling 2017: not checked.

### pmid-41701878 — CFAP46, MYO18B, TBC1D28: a WGS GWAS of 3,703 adults aged 90+ against 22,354 aged 18–75 (Russia), not seed loci

- **Why:** A whole-genome sequencing GWAS of longevity and 'healthy longevity' names variants in CFAP46 (with APOE, APOC1) against longevity and in MYO18B, TBC1D28 and LOC105376454 for healthy longevity. None of the four is a seed locus or a row. The abstract says 'significant' without a threshold, so whether any of them is genome-wide is unknown.
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Kashtanova D et al., "Longevity vs. Healthy Longevity: Different Outcomes Underlain by Different Mechanisms." *Aging and disease*, 2026 Feb 14. PMID 41701878, doi 10.14336/ad.2025.0828. Kashtanova 2026, the long-living adults' cohort; the second result sentence names MYO18B, TBC1D28 and LOC105376454.
    > Using whole-genome sequencing (WGS) and a genome-wide association study (GWAS), we found that variants with significant and negative associations with longevity in the GWAS were located in genes such as APOE, APOC1, and CFAP46, which are implicated in an increased risk of age-related diseases.
- **Unknown:** the threshold called significant, the rsIDs, effect sizes and replication, all of them full-text questions.

### row 96 APOE — ten uncited studies of survival and all-cause mortality, and one preprint

- **Why:** Each tests the row's own variants (rs429358, rs7412, and in two of them rs2075650) against mortality or survival to old age in a population or longevity cohort, and none is cited by the row. Ordered by size. The row is tier A, so these are corroboration, plus two non-European looks (Korea, Japan) and one null for ε4 in Koreans.
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Asiimwe IG et al., "APOE Genotype and Statin Response: Evidence From the UK Biobank and All of Us Program." *Clinical and translational science*, 2025 Aug. PMID 40763922, doi 10.1111/cts.70314. UK Biobank (389,843–452,189) and All of Us.
    > In UKB, ε3ε4 (HR: 1.08, 95% CI: 1.01-1.15) and ε4ε4 (HR: 1.54, 95% CI: 1.33-1.78) carriers had higher all-cause mortality risk.
  - Rasmussen KL et al., "Plasma levels of apolipoprotein E, APOE genotype, and all-cause and cause-specific mortality in 105 949 individuals from a white general population cohort." *European heart journal*, 2019 Sep 1. PMID 31236578, doi 10.1093/eurheartj/ehz402. 105,949 Danes from the general population.
    > We confirmed the well-known association between APOE genotypes and mortality.
  - Régy M et al., "The role of dementia in the association between APOE4 and all-cause mortality: pooled analyses of two population-based cohort studies." *The lancet. Healthy longevity*, 2024 Jun. PMID 38824957, doi 10.1016/s2666-7568(24)00066-7. Whitehall II and Three-City, pooled; dementia's share in the ε4 mortality effect.
    > Of these participants, APOE4 carriers (3264 [23%] of the cohort carried at least one ε4 allele) had a higher risk of all-cause mortality compared with non-carriers, with hazard ratios (HR) of 1·16 (95% CI 1·07-1·26) for heterozygotes and 1·59 (1·24-2·06) for homozygotes.
  - Shadyab AH et al., "Replication of Genome-Wide Association Study Findings of Longevity in White, African American, and Hispanic Women: The Women's Health Initiative." *The journals of gerontology. Series A, Biological sciences and medical sciences*, 2017 Oct 1. PMID 27707806, doi 10.1093/gerona/glw198. Women's Health Initiative, 11,053 women, survival to 85 and 90; its Hispanic arm bears on row 33 (listed again in the single-studies entry).
    > Among white women, three single nucleotide polymorphisms (SNPs) (rs2075650 [TOMM40], rs4420638 [APOC1], and rs429358 [APOE]) were significantly associated with survival to 90 years after correction for multiple testing (p < .001); rs4420638 and rs429358 were also significantly associated with healthy aging (p = .02).
  - Kulminski AM et al., "APOE ɛ4 allele and TOMM40-APOC1 variants jointly contribute to survival to older ages." *Aging cell*, 2022 Dec. PMID 36330582, doi 10.1111/acel.13730. Four US studies, survival to 85+, ε4 by rs2075650 (TOMM40) compound genotypes.
    > Consistent with our prior findings for AD, we show here that the adverse effect of the ɛ4 allele on survival to older ages is significantly higher in carriers of minor alleles of rs2075650 and/or rs12721046 polymorphisms compared with their non-carriers.
  - Choi CK et al., "The Association between the Apolipoprotein E Gene Polymorphism and All-cause Mortality in the Korean Population." *Journal of Korean medical science*, 2019 Oct 21. PMID 31625294, doi 10.3346/jkms.2019.34.e269. Two Korean population cohorts: ε2 HR 0.84, ε4 HR 1.08 (CI crossing 1).
    > In two large population-based cohort studies, the E2 allele was associated with a lower risk of mortality compared with the E3 allele, whereas the E4 genotype was not associated with mortality in Koreans.
  - Sasaki T et al., "Sex-Specific Effects of Apolipoprotein ε4 Allele on Mortality in Very Old and Centenarian Japanese Men." *The journals of gerontology. Series A, Biological sciences and medical sciences*, 2020 Sep 25. PMID 31603980, doi 10.1093/gerona/glz242. Japanese 85–99 year olds and 930 centenarians, men only.
    > The association analysis between APOE ε4 allele carriers and all-cause mortality indicated that APOE ε4 carriers showed significantly higher mortality rates than the APOE ε4 noncarriers among men in the very old group.
  - Ryu S et al., "Genetic landscape of APOE in human longevity revealed by high-throughput sequencing." *Mechanisms of ageing and development*, 2016 Apr. PMID 26930295, doi 10.1016/j.mad.2016.02.010. APOE resequenced in 450 Ashkenazi centenarians against controls.
    > Genotyping analysis of rs7412 and rs429358 showed significant enrichment of ε2 allele (p=0.003) and ε2/ε3 genotype (p=0.005), and significant depletion of ε3/ε4 genotype (p=0.005) in centenarians.
  - Tan Q et al., "Cohort Differences in the Associations of Selected Candidate Genes With Risk of All-Cause Mortality at Advanced Ages." *American journal of epidemiology*, 2020 Jul 1. PMID 31971580, doi 10.1093/aje/kwaa007. Danish 1905 and 1915 birth cohorts, mortality from 95 to 103.
    > Our estimated significant cohort effect on APOE$\varepsilon $4 is indicative of the interplay between the gene and the changing environment that modulates survival at extreme ages.
  - medRxiv preprint, "Level of Physical Activity and ApoE Status - Effects on Alzheimer's Disease and on Mortality." doi 10.64898/2026.06.18.26355781, posted 2026-06-22 (medRxiv's own listing, read 2026-11-17; not published, the API's `published` NA). Million Veteran Program, 137,593 veterans aged 65+, the outcome incident dementia **or** all-cause death combined, so not mortality alone. A preprint: never a replication.
    > Each additional APOE {varepsilon}4 allele was associated with a 19% increase in risk (aHR = 1.19, 95% CI 1.17-1.21), while active individuals had a 33% lower risk compared to inactive individuals (aHR = 0.67, 95% CI 0.66-0.68).
  - Dankner R et al., "ApoE Genotype, Lipid Profile, Exercise, and the Associations With Cardiovascular Morbidity and 18-Year Mortality." *The journals of gerontology. Series A, Biological sciences and medical sciences*, 2020 Sep 25. PMID 31585002, doi 10.1093/gerona/glz232. Israel, 949 survivors of a cohort, mean age 72; ε4 in men only, CI crossing 1.
    > In men only, ApoE E4 associated with CVD (adjusted odds ratio = 1.46, 95% confidence interval [CI] 0.76, 2.80) and with 18-year mortality (adjusted hazard ratio = 1.47, 95% CI 0.95, 2.26), adjusting for age, ethnicity, physical activity, hypertension, diabetes, low-density lipoprotein (LDL)-cholesterol, high-density lipoprotein (HDL)-cholesterol, triglycerides and lipid-lowering medications.

### row 43 FOXO3 — eleven uncited studies: mortality, longevity in East Asian and other cohorts, function of rs2802292

- **Why:** The row's lead rs2802292 (and its haplotype block) tested against mortality or longevity, or functionally, and none cited by the row (tier B). Two mortality studies in older Chinese adults (very likely one cohort) report the same protective GG direction, and American men of Japanese ancestry give a haplotype hazard ratio. The Sardinian Blue Zone and the Chinese gene-wide study are nulls or sex-limited, which bear on replication.
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Chen R et al., "FOXO3 longevity genotype mitigates the increased mortality risk in men with a cardiometabolic disease." *Aging*, 2020 Dec 1. PMID 33260156, doi 10.18632/aging.202175. 3,584 American men of Japanese ancestry, mortality by FOXO3 haplotype, larger effect with cardiometabolic disease.
    > Follow-up until Dec 31, 2019 found that in CMD-affected individuals, longevity-associated alleles of FOXO3 were associated with significantly longer lifespan: haplotype hazard ratio 0.81 (95% CI 0.72-0.91; diabetes 0.77, hypertension 0.82, CHD 0.83).
  - Ji JS et al., "Comparing Effects of FOXO3 and Residing in Urban Areas on Longevity: A Gene-Environment Interaction Study." *The journals of gerontology. Series A, Biological sciences and medical sciences*, 2022 Aug 12. PMID 34875051, doi 10.1093/gerona/glab362. Older Chinese adults, rs2802292 GG HR 0.81 (the abstract does not name the cohort).
    > We found the minor allele homozygotes of FOXO3 to have a protective effect on mortality (HR [95% CI] for rs4946936 TT vs CC: 0.807 [0.653-0.996]; rs2802292 GG vs TT: 0.812 [0.67-0.985]; rs2253310 CC vs GG: 0.808 [0.667-0.978]).
  - Liu L et al., "Gene-Environment Interaction of FOXO and Residential Greenness on Mortality Among Older Adults." *Rejuvenation research*, 2021 Feb. PMID 32364002, doi 10.1089/rej.2019.2301. Older Chinese adults, the same three SNPs and hazard ratios, very likely an overlapping sample with the entry above.
    > We found that participants carrying two minor alleles of the three studied FOXO3A SNPs had lower mortality risk than those without minor allele (hazard ratio [HR]: 0.803 95% confidence interval [CI]: 0.654-0.987 for rs4946936, HR: 0.807 95% CI: 0.669-0.974 for rs2802292, HR: 0.803 95% CI: 0.666-0.968 for rs2253310).
  - Willcox BJ et al., "Longevity-Associated FOXO3 Genotype and its Impact on Coronary Artery Disease Mortality in Japanese, Whites, and Blacks: A Prospective Study of Three American Populations." *The journals of gerontology. Series A, Biological sciences and medical sciences*, 2017 May 1. PMID 27694344, doi 10.1093/gerona/glw196. rs2802292 G against coronary death in Japanese, White and Black Americans.
    > Multivariate Cox regression models demonstrated that carriage of the longevity-associated G allele of FOXO3 single nucleotide polymorphisms rs2802292 was a protective factor against CAD mortality in all three populations.
  - Li N et al., "Association study of polymorphisms in FOXO3, AKT1 and IGF-2R genes with human longevity in a Han Chinese population." *Oncotarget*, 2016 Jan 5. PMID 26683100, doi 10.18632/oncotarget.6627. Han Chinese long-lived against controls; rs9486902 is not the row's lead.
    > Rs9486902 of FOXO3 was found to be associated with human longevity in both genders combined in this study (allelic P = 0.002, corrected P = 0.024).
  - Lin R et al., "Genetic Association Analysis of Common Variants in FOXO3 Related to Longevity in a Chinese Population." *PloS one*, 2016. PMID 27936216, doi 10.1371/journal.pone.0167918. Chinese, FOXO3 gene-wide: nothing in both sexes, five SNPs in men only.
    > However, when stratifying by gender, four SNPs (rs10499051, rs7762395, rs4946933 and rs3800230) previously reported to be associated with longevity and one novel SNP (rs4945815) showed significant association with male longevity (P-values: 0.007-0.032), but all SNPs were not associated with female longevity.
  - He YH et al., "Association of the insulin-like growth factor binding protein 3 (IGFBP-3) polymorphism with longevity in Chinese nonagenarians and centenarians." *Aging*, 2014 Nov. PMID 25553725, doi 10.18632/aging.100703. Chinese nonagenarians and centenarians, rs13217795.
    > Our results confirm the association of the forkhead box O3 (FOXO3) variant (rs13217795) and the ATM serine/threonine kinase (ATM) variant (rs189037) genotypes with longevity (p=0.0075 and p=0.026, using the codominant model and recessive model, respectively).
  - Kolovou V et al., "Five gene variants in nonagenarians, centenarians and average individuals." *Archives of medical science : AMS*, 2017 Aug. PMID 28883855, doi 10.5114/aoms.2017.68942. 256 nonagenarians and centenarians against 149 controls, rs13217795 and rs2764264 (the population is not named in the abstract).
    > Furthermore, in the study group, the T allele was significantly more frequent in the nonagenarians (n = 239) than the centenarians (n = 17) in both FOXO3A; rs13217795 and rs2764264 (64.4 vs. 44.1%, p = 0.018 and 69.7 vs. 50.0%, p = 0.017, respectively).
  - Errigo A et al., "Lack of association between common polymorphisms associated with successful aging and longevity in the population of Sardinian Blue Zone." *Scientific reports*, 2024 Dec 28. PMID 39730495, doi 10.1038/s41598-024-80497-w. Sardinian Blue Zone, rs2802292 among 11 markers: null.
    > Overall, the findings of this study do not support a significant association of known genetic variants on survival in the population of the Sardinian LBZ, suggesting that other genetic or epigenetic traits not yet identified might play a role.
  - Torigoe TH et al., "Novel protective effect of the FOXO3 longevity genotype on mechanisms of cellular aging in Okinawans." *npj aging*, 2024 Mar 8. PMID 38459055, doi 10.1038/s41514-024-00142-8. Okinawans, rs2802292 G with telomerase activity and telomere length; function, not outcome.
    > This was accompanied by higher levels of telomerase activity in mononuclear cells for carriers of the longevity-associated FOXO3 G-allele of SNP rs2802292 (P = 0.015).
  - Santo EE et al., "FOXO3A-short is a novel regulator of non-oxidative glucose metabolism associated with human longevity." *Aging cell*, 2023 Mar. PMID 36617632, doi 10.1111/acel.13763. FOXO3A-Short isoform and rs9400239 (not a row rsID): function in Danish twins.
    > Assessment of the relationship between the FOXO3A-S polymorphism and peripheral glucose clearance during insulin infusion (Rd clamp) in a cohort of Danish twins revealed that longevity T-allele carriers have markedly faster peripheral glucose clearance rates than normal lifespan C-allele carriers.

### row 73 KL (KL-VS) — six uncited studies, three of them nulls for the row's variant

- **Why:** Row 73 (tier C) rests on KL-VS (rs9536314). Newcastle 85+ with UK Biobank finds KL-VS not associated with reaching very old age, MrOS Sweden finds rs9536314 not associated with mortality, Sardinia is null, and Korea has no KL-VS at all, which bears on the row's ancestry context. None is cited by the row.
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Amin HA et al., "No Evidence That Genetic Variation at the Klotho Locus Is Associated With Longevity in Caucasians from the Newcastle 85+ Study and the UK Biobank." *The journals of gerontology. Series A, Biological sciences and medical sciences*, 2022 Mar 3. PMID 34893828, doi 10.1093/gerona/glab361. Newcastle 85+ against UK Biobank: KL-VS null, two other KL SNPs associated.
    > We found that the rs2283368 CC genotype and the rs9536338 C allele, but not the KL-VS haplotype, were associated with reaching very old age.
  - Wu PH et al., "The association between Single Nucleotide Polymorphisms of Klotho Gene and Mortality in Elderly Men: The MrOS Sweden Study." *Scientific reports*, 2020 Jun 24. PMID 32581247, doi 10.1038/s41598-020-66517-5. MrOS Sweden men, all-cause and cardiovascular mortality: null.
    > In conclusion, these two potentially damaging SNPs (rs9536314 and rs9527025) in the KL gene were not associated with all-cause mortality or cardiovascular mortality in MrOs cohort.
  - Errigo A et al., "Lack of association between common polymorphisms associated with successful aging and longevity in the population of Sardinian Blue Zone." *Scientific reports*, 2024 Dec 28. PMID 39730495, doi 10.1038/s41598-024-80497-w. Sardinian Blue Zone nonagenarians, KLOTHO rs9536314 among 11 markers: null.
    > Overall, the findings of this study do not support a significant association of known genetic variants on survival in the population of the Sardinian LBZ, suggesting that other genetic or epigenetic traits not yet identified might play a role.
  - Kim HK et al., "Lack of functional KL-VS polymorphism of the KLOTHO gene in the Korean population." *Genetics and molecular biology*, 2016 Jul-Sep. PMID 27560364, doi 10.1590/1678-4685-gmb-2015-0160. Monomorphic in Koreans.
    > The KL-VS variant was not found in 874 Korean individuals.
  - Pereira RMR et al., "KLOTHO polymorphisms and age-related outcomes in community-dwelling older subjects: The São Paulo Ageing & Health (SPAH) Study." *Scientific reports*, 2020 May 22. PMID 32444684, doi 10.1038/s41598-020-65441-y. São Paulo older adults, three KLOTHO SNPs (C370S is in the KL-VS haplotype) against ageing outcomes and mortality; the result sentence for mortality names no genotype effect.
    > This study evaluated three KLOTHO polymorphisms, namely G395A, C1818T, and C370S, in an elderly population (mean age of 73 years) and their associations with ageing-related outcomes (cardiovascular events, kidney function, osteoporosis, sarcopenia) and mortality.
  - Yokoyama JS et al., "Systemic klotho is associated with KLOTHO variation and predicts intrinsic cortical connectivity in healthy human aging." *Brain imaging and behavior*, 2017 Apr. PMID 27714549, doi 10.1007/s11682-016-9598-2. Healthy older adults: serum klotho by KL-VS genotype, lower in homozygotes; function, not outcome.
    > Serum klotho levels were increased with KL-VS heterozygosity, as anticipated.
- **Unknown:** 32444684's genotype results, which the abstract does not state.

### row 59 ABO — two uncited Chinese longevity studies, one positive, one null

- **Why:** Row 59 (tier B, lead rs2519093). CLHLS, 5,803 long-lived against 7,026 controls, reports four ABO variants (rs8176719 among them, the O-allele deletion) with replication in the CLHLS GWAS; a second Chinese study of 2,201 centenarians finds no association. Whether either tags rs2519093 is unknown.
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Ni X et al., "Identification and replication of novel genetic variants of ABO gene to reduce the incidence of diseases and promote longevity by modulating lipid homeostasis." *Aging*, 2021 Nov 22. PMID 34812738, doi 10.18632/aging.203700. CLHLS, ≥90 without adverse outcomes, discovery and GWAS replication.
    > Four ABO gene variants associated with healthy longevity (rs8176719 C, rs687621 G, rs643434 A, and rs505922 C) were identified and replicated in the CLHLS GWAS data analysis and found significantly higher in longevity individuals than controls.
  - Zhu Y et al., "Allelic distribution of ABO gene in Chinese centenarians." *Aging medicine (Milton (N.S.W))*, 2020 Sep. PMID 33103040, doi 10.1002/agm2.12122. 2,201 Chinese centenarians: null.
    > Integrated with other previous reports, we conclude from this large Chinese cohort that genetic variants of the ABO gene and blood groups are not associated with longevity.
- **Unknown:** LD between the four CLHLS variants and rs2519093 in East Asians.

### row 46 LPA — two uncited studies: the LPA locus against parental lifespan and healthspan, and rs10455872 against mortality

- **Why:** Row 46 (tier A, rs10455872 and rs55730499). Arsenault 2020 builds a 26-SNP LPA score and finds it inversely associated with parental lifespan in UK Biobank (P 2.7e-8) and with healthspan; Langsted 2019 tests Lp(a) and its genetic instruments against mortality in two Danish general-population studies (119,094 genotyped for rs10455872). Whether either sample overlaps the row's evidence is not checked.
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Arsenault BJ et al., "Association of Long-term Exposure to Elevated Lipoprotein(a) Levels With Parental Life Span, Chronic Disease-Free Survival, and Mortality Risk: A Mendelian Randomization Analysis." *JAMA network open*, 2020 Feb 5. PMID 32108890, doi 10.1001/jamanetworkopen.2020.0129. UK Biobank 139,362; also health span and EPIC-Norfolk mortality.
    > In 139 362 white British participants (mean [SD] age, 62.8 [3.9] years; 52% women) from the UK Biobank, increases in the genetic risk score (weighted for a 50-mg/dL increase in Lp[a] levels) were inversely associated with a high parental life span (odds ratio, 0.92; 95% CI, 0.89-0.94;
  - Langsted A et al., "High lipoprotein(a) and high risk of mortality." *European heart journal*, 2019 Sep 1. PMID 30608559, doi 10.1093/eurheartj/ehy902. Two Danish general-population studies; for cardiovascular mortality the KIV-2 instrument is associated, rs10455872 is not (0.98).
    > For cardiovascular mortality, a 50 mg/dL (105 nmol/L) increase in lipoprotein(a) levels was associated observationally with a hazard ratio of 1.16 (1.09-1.23), and genetically with risk ratios of 1.23 (1.08-1.41) based on LPA KIV2 and of 0.98 (0.88-1.09) based on LPA rs10455872.

### row 84 CETP — two uncited studies of the CETP deficiency alleles

- **Why:** Row 84 (tier C, rs3764261). A Danish genetic CETP-deficiency score against cardiovascular and all-cause mortality, and I405V against age in blood donors and older adults (null).
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Nordestgaard LT et al., "Long-term Benefits and Harms Associated With Genetic Cholesteryl Ester Transfer Protein Deficiency in the General Population." *JAMA cardiology*, 2022 Jan 1. PMID 34613338, doi 10.1001/jamacardio.2021.3728. Danish cohorts, a CETP allele score; benefits and harms (age-related macular degeneration).
    > Multivariable adjusted hazard ratios showed that a genetically lower level of non-HDL cholesterol (ie, 17 mg/dL) was associated with a lower risk of cardiovascular mortality (hazard ratio [HR], 0.77 [95% CI, 0.62-0.95]), ischemic heart disease (HR, 0.80 [95% CI, 0.68-0.95]), myocardial infarction (HR, 0.72 [95% CI, 0.55-0.93]), peripheral arterial disease (HR, 0.80 [95% CI, 0.63-1.02]), and vascular dementia (HR, 0.38 [95% CI, 0.18-0.80]) and an increased risk of AMD (HR, 2.33 [95% CI, 1.63-3.30]) but was not associated with all-cause mortality (HR, 0.91 [95% CI, 0.81-1.02]), ischemic stroke (HR, 1.05 [95% CI, 0.81-1.36]), or Alzheimer disease (HR, 1.25 [95% CI, 0.89-1.76]).
  - Bustami J et al., "Cholesteryl ester transfer protein (CETP) I405V polymorphism and cardiovascular disease in eastern European Caucasians - a cross-sectional study." *BMC geriatrics*, 2016 Jul 20. PMID 27439317, doi 10.1186/s12877-016-0318-y. I405V against age in blood donors and older adults: null.
    > We could not find any association of this polymorphism with age for both, males or females, in any of these cohorts (P = 0.71 and P = 0.57, respectively, for males and P = 0.55 and P = 0.88, respectively, for females).

### row 48 IL6 — three uncited studies of other IL6 promoter SNPs and longevity

- **Why:** Row 48 (tier D) carries rs2069837. These test −174G/C (rs1800795) and rs1800796, not the row's variant: a meta-analysis and a three-cohort centenarian study are null for rs1800795, and a small Uyghur study reports rs1800796. They bear on the gene, not the row's lead, so the curator decides whether they belong.
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Wei GZ et al., "Association of longevity with TNF-α G308A and IL-6 G174C polymorphic inflammatory biomarkers in Caucasians: a meta-analysis." *Zeitschrift fur Gerontologie und Geriatrie*, 2016 Dec. PMID 26754162, doi 10.1007/s00391-015-0992-y. Meta-analysis, long-lived ≥80.
    > We found no evidence that the TNF-α G308A and IL-6 G174C SNPs affected the probability of reaching an advanced age in Caucasians, and that they have little effect on delaying the onset and progression of age-related diseases, but this does not rule out the possibility of population-specific effects caused by different genes and/or environmental factors and their interactions.
  - Fuku N et al., "Exceptional longevity and muscle and fitness related genotypes: a functional in vitro analysis and case-control association replication study with SNPs THRH rs7832552, IL6 rs1800795, and ACSL1 rs6552828." *Frontiers in aging neuroscience*, 2015. PMID 25999849, doi 10.3389/fnagi.2015.00059. Spanish, Italian and Japanese centenarians.
    > Yet we found no significant association of EL with rs7832552, rs1800795 or rs6552828 in any of the 3 cohorts.
  - Gulizibaer M et al., "[Association of single nucleotide polymorphisms of IL-6 gene with longevity in Uyghurs in Xinjiang]." *Zhonghua yi xue za zhi*, 2015 Nov 10. PMID 26813132. 240 Uyghurs ≥90 against 92 controls.
    > CT genotype of rs1800796 was positively associated with longevity (Padd=0.002, OR=1.983, 95%CI: 1.296-3.023), while no significant association was noted between other genotypes and longevity.

### rows 23 TERC, 30 TERT, 160 STN1/OBFC1 — telomere-length alleles against mortality and survival

- **Why:** The telomere-length rows sit in the unscored marker section. Rode 2015 tests a TERC/TERT/OBFC1 allele sum (rs1317082, rs7726159, rs2487999; whether these tag the rows' leads is unknown) against all-cause mortality in 64,637 Danes: null. Scarabino 2019 ties TERT rs2853691 and MNS16A to dying before 90. Druley 2016 reports a rare OBFC1 3′UTR variant with exceptional survival in LLFS pedigrees.
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Rode L et al., "Peripheral blood leukocyte telomere length and mortality among 64,637 individuals from the general population." *Journal of the National Cancer Institute*, 2015 Jun. PMID 25862531, doi 10.1093/jnci/djv074. Copenhagen, 64,637.
    > Allele sum was not associated with cardiovascular, other, or all-cause mortality.
  - Scarabino D et al., "Analysis of the Association Between TERC and TERT Genetic Variation and Leukocyte Telomere Length and Human Lifespan-A Follow-Up Study." *Genes*, 2019 Jan 25. PMID 30691026, doi 10.3390/genes10020082. Older adults, nine-year follow-up, age at death (the abstract does not name the population).
    > TERT VNTR MNS16A L/L genotype and TERT rs2853691 A/G or G/G genotypes were found to be associated with a significantly higher risk to die before the age of 90 years, and with a significantly lower age at death.
  - Druley TE et al., "Candidate gene resequencing to identify rare, pedigree-specific variants influencing healthy aging phenotypes in the long life family study." *BMC geriatrics*, 2016 Apr 9. PMID 27060904, doi 10.1186/s12877-016-0253-y. LLFS, 615 pedigrees; rare, pedigree-specific.
    > Most notably, we found a novel variant significantly associated with exceptional survival in the 3' UTR OBFC1 in 13 individuals from six pedigrees.

### row 159 HLA-DQB1 (and 38 HLA-DQA1) — two uncited HLA longevity studies

- **Why:** Row 159 (tier C, rs9275160). Yang 2017 reports four HLA-DQB1 SNPs with longevity in a Chinese longevity cohort from exome sequencing; the IHIW workshop reports HLA alleles and haplotypes, DQA1 included, with healthy ageing in four populations (small samples).
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Yang F et al., "Identification of new genetic variants of HLA-DQB1 associated with human longevity and lipid homeostasis-a cross-sectional study in a Chinese population." *Aging*, 2017 Nov 10. PMID 29129831, doi 10.18632/aging.101323. Chinese Longevity Cohort, exome then Sanger.
    > Through whole-exome sequencing and sanger sequencing genotypes, we identified four new single nucleotide polymorphisms of HLA-DQB1(major histocompatibility complex, class II, DQ beta 1), rs41542812 rs1049107 rs1049100 rs3891176(Prange=0.048-2.811×10-8 for allele frequencies), associated with longevity in Chinese Longevity Cohort.
  - Ivanova M et al., "17th IHIW component "Immunogenetics of Ageing" - New NGS data." *Human immunology*, 2019 Sep. PMID 31331679, doi 10.1016/j.humimm.2019.07.287. 17th IHIW, allele-level HLA in healthy elderly against young controls.
    > These preliminary NGS data could confirm our hypotheses that survival and longevity might be associated with selection of HLA alleles and haplotypes conferring disease resistance or susceptibility.

### single uncited studies at rows 114 TFAM, 6 CELSR2, 33 EBF1, 83 FTO, 25 HTT, 57 CDKN2B-AS1 and 80 CHRNB4

- **Why:** One study each that bears on the row and that the row does not cite. CELSR2's is the row's own rs646776 in a PheWAS across 23andMe and UK Biobank; TFAM's is rs1937 (not the row's rs12247015) in Chinese oldest-old; HTT's is intermediate CAG alleles, not the row's SNPs; CDKN2B-AS1's is functional (rs1537371, not a row rsID); CHRNB4's is the 15q25 rs1051730 locus against mortality in Finnish smokers, adjacent to the row. EBF1's is SNPs in LD with the row's rs2149954 against survival to 85 in Hispanic women (WHI); FTO's is a meta-analysis of rs9939609 (not the row's rs1421085 or rs11642015, which are near it) against all-cause mortality, null after adiposity adjustment.
- **Found by:** the 2015-01-01 → 2026-10-20 backfill (lead, 2026-11-17), its queries in `scout/SEARCHES.md`; abstracts read through PubMed E-utilities 2026-11-17. None of these PMIDs is cited by a row, held in `corpus/` or in a track's CSV.
- **Papers**, strongest first:
  - Li QS et al., "The association of clinical phenotypes to known AD/FTD genetic risk loci and their inter-relationship." *PloS one*, 2020. PMID 33152005, doi 10.1371/journal.pone.0241552. row 6: AD/FTD loci PheWAS, 23andMe and UK Biobank.
    > APOE variants defining ε2/ε3/ε4 alleles and rs646776 were identified to be significantly associated with metabolic/cardiovascular and longevity traits.
  - Shadyab AH et al., "Replication of Genome-Wide Association Study Findings of Longevity in White, African American, and Hispanic Women: The Women's Health Initiative." *The journals of gerontology. Series A, Biological sciences and medical sciences*, 2017 Oct 1. PMID 27707806, doi 10.1093/gerona/glw198. row 33: WHI, survival to 85.
    > In Hispanic women, 7 SNPs in linkage disequilibrium with a novel SNP, rs2149954, recently identified as being associated with increased longevity in a European population, were significantly associated with decreased survival to age 85 for carriers of the T versus C allele (p = .04).
  - Zimmermann E et al., "Is the adiposity-associated FTO gene variant related to all-cause mortality independent of adiposity? Meta-analysis of data from 169,551 Caucasian adults." *Obesity reviews : an official journal of the International Association for the Study of Obesity*, 2015 Apr. PMID 25752329, doi 10.1111/obr.12263. row 83: meta-analysis, 169,551 adults.
    > In conclusion, this study does not support that the FTO SNP is associated with all-cause mortality independently of the adiposity phenotypes.
  - Chen Q et al., "Association between single nucleotide polymorphism of rs1937 in TFAM gene and longevity among the elderly Chinese population: based on the CLHLS study." *BMC geriatrics*, 2022 Jan 3. PMID 34979947, doi 10.1186/s12877-021-02655-3. row 114: Chinese long-lived against younger elderly.
    > Binary logistic regression analysis showed that compared to younger elderly, the long-lived individuals with "CC genotype" of rs1937 were more closely related to increased longevity than those with "GG genotype" (OR: 1.989, 95% CI: 1.160-3.411).
  - Ingannato A et al., "Intermediate alleles of HTT: A new pathway in longevity." *Journal of the neurological sciences*, 2022 Jul 15. PMID 35580427, doi 10.1016/j.jns.2022.120274. row 25: HTT intermediate alleles, centenarians against controls with cognitive decline.
    > Our data show a statistically significant higher frequency of IAs in Centenarians with respect to pathological controls with cognitive decline (p = .031;
  - Jiang D et al., "Post-GWAS functional analysis identifies CUX1 as a regulator of p16INK4a and cellular senescence." *Nature aging*, 2022 Feb. PMID 37117763, doi 10.1038/s43587-022-00177-0. row 57: CUX1 at the CDKN2A/B lifespan locus.
    > We demonstrate that transcription factor CUX1 (Cut-Like Homeobox 1) specifically binds to an atherosclerosis-associated functional single-nucleotide polymorphism (fSNP) (rs1537371) within the locus and regulates the CDKN2A/B-encoded proteins p14ARF, p15INK4b and p16INK4a and the antisense noncoding RNA in the CDK4 (INK4) locus (ANRIL) in endothelial cells (ECs).
  - Kupiainen H et al., "CHRNA5/CHRNA3 Locus Associates with Increased Mortality among Smokers." *COPD*, 2016 Aug. PMID 26751916, doi 10.3109/15412555.2015.1049260. row 80: COPD patients and long-term smokers.
    > Homozygosity for the risk allele was associated in both cohorts with all-cause mortality (crude HR 2.2, 95% CI 1.2-3.8 and 1.3, 95% CI 1.1-1.5, respectively), with any type of cancer (crude OR 2.3, 95% CI 1.0-5.1) among the COPD patients and with the number of pack-years (crude OR 1.4, 95% CI 1.1-1.9) among the male smokers.


### doi-10.64898/2026.08.24.26361177 — HLA-DRB1*15:01 (row 135) and HLA-DQA1 (row 38): HLA-II haplotypes in centenarians, a preprint

- **Closed** 2026-11-17 (curator, 0b389c2, `corpus/doi-10.64898_2026.08.24.26361177.md`): read at abstract depth, the full text unreachable (medRxiv 403 on every route, Europe PMC PPR1306907 full text 500). Rows 135 and 38 unmoved: Hap-Y has only the microglial finding, Hap-R the longevity one, and no tag SNP is named, so both readings are unknown, not null. Kept on the scout's published-version watch; the curator re-reads when a full text opens.

- **Paper:** Alvarez Sirvent D, Luimes MC, Tesi N, et al. "Fine-mapping HLA-II haplotypes in Alzheimer's disease and healthy longevity reveals
  distinct associations with microglial HLA-II load and neuropathology." medRxiv, v1 2026-08-27, v2 2026-10-09, doi
  10.64898/2026.08.24.26361177; not published (bioRxiv API `published` NA, Crossref and Europe PMC: none, 2026-11-17).
  In track E's evidence CSV; row 135 does not cite it. Track E rerun, 2026-11-17.
- **Why:** it fine-maps six HLA-II haplotypes in 443 cognitively healthy centenarians, 3,219 population controls and
  2,391 AD patients (Dutch), and names Hap-Y as DRB1*15:01, row 135's allele. The abstract gives Hap-Y only a microglial
  finding; whether Hap-Y differs between centenarians and controls, and in which direction, is not in it. It also says Hap-R (DRB1*01:01) "reduced healthy longevity" and that three
  haplotypes overlap earlier lifespan signals, without naming which: row 38 HLA-DQA1 (rs34831921, rs34967069,
  rs28383322, the HLA-DQA1/DRB1 parental-lifespan locus) may be one. v2's abstract is word for word v1's, so the
  version itself adds nothing seen here; the reason to read it is that rows 135 and 38 cite neither version. Track E's
  evidence CSV (row 11) gives Hap-Y only "microglial HLA-II activation", no centenarian result. A preprint: never a
  replication; watched for its published version.
- **Passage** (abstract, v2, https://doi.org/10.64898/2026.08.24.26361177, through the bioRxiv API, read 2026-11-17):
  > Hap-Y (DRB1*15:01) showed increased microglial HLA-II activation in post-mortem brain tissue, independent of quantitative AD neuropathology.
- **Unknown:** Hap-Y's centenarian-versus-control result; whether Hap-Y is the haplotype rs3135388 tags; which three
  haplotypes overlap earlier lifespan signals, and whether Hap-R is row 38's signal. Licence CC BY-NC-ND (the API's field).
  Each is settled by the full text or its supplement.

### pmid-42928374 — FES/FURIN (locus 81): pleiotropy with severe mental disorders

- **Closed** 2026-11-16 (curator, 7741c02): FURIN's shared variant is with telomere length (gLTL) in all three disorders, not mvAge (Table 2, corpus/pmid-42928374 q1 to q3), so row 81 is not re-read. The lead SNP sits in Supplementary Tables 2 to 15, which the publisher refuses (403), so whether it is rs6224, rs17514846 or a tag is unknown. Open access, CC BY-NC-ND.

- **Paper:** Pisanu C, Nishioka M, et al. "Genome-wide analysis identifies pleiotropic genes shared between severe
  mental disorders and biomarkers of cellular aging." *Mol Psychiatry*, 2026 Oct 25 (online ahead of print).
  PMID 42928374, doi 10.1038/s41380-026-03946-0. Track E sweep, 2026-11-10 (E-core).
- **Why:** FURIN is named among nine genes carrying variants shared between "aging biomarkers" and all three
  disorders (bipolar disorder, MDD, schizophrenia). The biomarkers studied are mvAge (the multivariate longevity
  factor), brain-age gap, telomere length, mtDNA copy number and epigenetic age acceleration; the abstract does not
  say which of them FURIN's variant is shared with. If mvAge, this bears on the pleiotropy axis of the FES/FURIN row
  (track H counts rs6224 among the few lifespan leads with almost no disease footprint); if a clock or brain age,
  it is in a class track E keeps out of scoring.
- **Passage** (abstract, PubMed, https://pubmed.ncbi.nlm.nih.gov/42928374/, read 2026-11-10):
  > We identified several pleiotropic variants, with nine genes (AC068490.2, ASIC2, CNNM2, FURIN, GPM6A, HS6ST3, RP5-1043L13.1, SORCS3 and SP4) containing variants shared between aging biomarkers and all disorders.
- **Unknown:** which biomarker FURIN's variant is shared with; whether that variant is rs6224 or rs17514846 (the seed's
  variants), or in LD with them (the abstract names no rsID); whether the article is open access (a "© The
  Author(s)" line does not show a licence). Each is settled by the full text or its supplementary tables.

### rs13141210 at locus 28 RNU1-63P (4q13.2): a second mvAge signal, candidate row (D25.6)

- **Taken:** row 162 RNU6-699P, `second_signal_of` 28 (D39.14; 352bfc5, tier C under D39.15 in a5d568c).

- **Paper:** Rosoff DB et al. "Multivariate genome-wide analysis of aging-related traits identifies novel loci and new
  drug targets for healthy aging." *Nat Aging*, 2023 Aug. PMID 37550455, PMC10432278, doi 10.1038/s43587-023-00455-5
  (title checked against PubMed 2026-11-11). Corpus note `corpus/pmid-37550455.md`. From the curator, 2026-11-11.
- **Why:** a genome-wide mvAge lead 111 kb from row 28's lead rs28637671 at r² 0.095, so a separate signal; a seed
  rsID with no seed locus of its own. Row 28 names it in prose; D25.6 sends it here, to be curated after the seed list.
  The row's prose reads it as a possible B under D16 (LifeGen z about 4.4).
- **Passage** (Table 1, full text, Europe PMC, read by the curator 2026-11-11; `pmid-37550455#q28`):
  > rs13141210 4,67891641 C/T 0.50 −0.0058 (0.001) 1.46 × 10−8 RNU6-699P (intergenic) 0.55 Adult body size, cognitive performance, education, household income, lung cancer
- **Unknown:** its own tier; whether its tag rs10434248 (aging-GIP1, Timmers 2022) counts as a second multivariate
  scan or a shared input.

### rs16843603 (ADD1) at locus 25 HTT (4p16.3): a second mvAge signal, candidate row (D25.6)

- **Taken:** row 163 ADD1, `second_signal_of` 25 (D39.14; 4f0bb15, tier C under D39.15).

- **Paper:** Rosoff 2023, as above (PMID 37550455). From the curator, 2026-11-11.
- **Why:** a genome-wide mvAge lead in an ADD1 intron, r² 0.095 to row 25's lead rs61348208, so a separate signal; a
  seed rsID with no seed locus of its own. Row 25 names it in prose; D25.6 sends it here.
- **Passage** (Supplementary table, MOESM3, read by the curator 2026-11-11; `pmid-37550455#q23`):
  > No (Frailty, Lifespan) rs16843603 11 4:2928577 4 2928577 7 rs16843603;rs2798287;rs11937729;rs1801058;rs113928896;rs71597207;rs34155847 C T 0.3052 4.1616324788e-10 -0.00705057367178 0.00112848149177 ADD1 0 intronic 3.773 5 4 4 2.83548326833141 4 0.585723327229924
- **Unknown:** its own tier; whether any lifespan study carries it outside mvAge's inputs (D16).

### rs114298671 (MSANTD1/RGS12) at locus 25 HTT (4p16.3): a third mvAge signal, candidate row (D25.6)

- **Taken:** row 164 MSANTD1, `second_signal_of` 25 (D39.14; 4f0bb15, tier C under D39.15).

- **Paper:** Rosoff 2023, as above (PMID 37550455). From the curator, 2026-11-11.
- **Why:** a genome-wide mvAge lead near MSANTD1, novel in Rosoff, r² 0.08 to row 25's lead rs61348208, so a separate
  signal; a seed rsID with no seed locus of its own. Row 25 names it in prose; D25.6 sends it here.
- **Passage** (Supplementary table, MOESM3, read by the curator 2026-11-11; `pmid-37550455#q24`):
  > Yes rs114298671 11 4:3281869 4 3281869 2 rs114298671;rs71597207 A G 0.1223 1.56686856265e-08 0.00886760197706 0.00156835563347 MSANTD1 8403 intergenic 0.873 5 5 15 1.82958854405307 4 0.767064731931399
- **Unknown:** its own tier; whether any lifespan study carries it outside mvAge's inputs (D16); it shares a tag,
  rs71597207, with rs16843603's set above, so whether the two are wholly separate is unsettled here.

### rs3131621 (MICA … MICB / HCP5) at locus 37 HCP5 (6p21.33): the fathers' signal, candidate row (D25.6)

- **Taken:** row 165 MICA/MICB, `second_signal_of` 37 (D39.14; b3f3ebc, tier C under D39.15).

- **Paper:** Pilling LC et al. "Human longevity: 25 genetic loci associated in 389,166 UK biobank participants."
  *Aging (Albany NY)*, 2017. PMID 29227965. Replication: Wright KM et al., *G3*, 2019, PMID 31484785. Corpus notes
  `corpus/pmid-29227965.md`, `corpus/pmid-31484785.md`. From the curator, 2026-11-11.
- **Why:** Pilling's fathers' lead, 278 kb from row 37's lead rs3130507 (the mothers' signal), with no Ensembl CEU pair
  above the 0.05 floor (`db-ensembl-116#q247`, `q248`; the endpoint answers pairs megabases apart, `q242`): a
  separate signal, and the seed's
  second rsID at locus 37 with no locus of its own. Row 37 names it in prose; D25.6 sends it here. It has the stronger
  case of the two: replicated in AncestryDNA's fathers (P 7.7e-4, meta-analysis 8.9e-9, Wright's Table 3), LifeGen
  with UK Biobank P 1.9e-6, Timmers' LifeGen-without-UK-Biobank fathers one-sided P 0.093; the GWAS Catalog also lists
  rheumatoid arthritis or inflammatory bowel disease there (P 2e-13, `db-gwascatalog-2026.10.29#q234`, `q235`).
- **Passage** (Table 2, full text, read by the curator 2026-11-11; not yet quoted in the note):
  > rs3131621 6 31425499 A G 8.9E-08 1.9E-02 4.8E-01 3.5E-05 3.6E-08 0.629 −0.0124 0.0022 MICA … MICB
- **Unknown:** its own tier (Deelen 2019 flat: 90th OR 1.0004, P 0.99, a flag under the APOE factor only, so none,
  by the curator's reading); its gene (Open Targets 26.09 has no record of it).

### rs15285 (LPL 3′ UTR) at locus 52 LPL (8p21.3): Wright's fathers' signal, candidate row (D25.6)

- **Taken:** row 166 LPL-3UTR, `second_signal_of` 52 (D39.14; d8fc413, filed at B).

- **Paper:** Wright KM et al. "A Prospective Analysis of Genetic Variants Associated with Human Lifespan." *G3*, 2019.
  PMID 31484785. Corpus note `corpus/pmid-31484785.md` (q91 to q93). From the curator, 2026-11-11.
- **Why:** the seed's second rsID at locus 52, 11 kb from row 52's lead rs268 (LPL Asn318Ser) and a separate signal:
  r² below 0.05 from the two frequencies (`db-ensembl-116#q364`), and Aragam 2022's coronary disease
  fine-mapping holds rs268 alone in one set and rs15285 in another (`db-opentargets-26.09#q671`, `q678`). It carries
  LPL's only lifespan-class genome-wide result: Wright's fathers' meta-analysis P 8.5e-10, T (0.29 in Europeans)
  longer-lived, heterogeneity P 0.83; the AncestryDNA arm (P 2.4e-5, 1.0e-4 after genomic control) is inside the pooled
  P. Row 52 names it in prose; D25.6 sends it here. T tags rs13702 (r² 0.98) and partly rs328 (0.33).
- **Passage** (Table 3, full text, quoted as `pmid-31484785#q91`):
  > LPL	rs15285	8	19824667	8.46e-10	2.44e-05	0.012	0.003	1.20e-07	0.013	0.002
- **Unknown:** its own tier. Nothing outside Wright replicates it nominally: Timmers 2019 P 3.5e-5 (holds UK
  Biobank), Deelen's 90th one-sided 0.065, FinnGen death one-sided 0.16 (APOE factor power 0.66, no red flag), so B by
  the curator's reading; Wright's PICS set is flat (PIP 0.066 of 25, C3), L2G LPL 0.98.

### rs11780471 (3.6 kb upstream of EPHX2) at locus 53 EPHX2 (8p21.1): Wright's fathers' signal, candidate row (D25.6)

- **Taken:** row 168 CHRNA2-EPHX2, `second_signal_of` 53 (D39.14; 8c08388, filed at C at most; D39.18).

- **Paper:** Wright KM et al. "A Prospective Analysis of Genetic Variants Associated with Human Lifespan." *G3*, 2019.
  PMID 31484785. Corpus note `corpus/pmid-31484785.md` (q99). From the curator, 2026-11-11.
- **Why:** 97 kb from row 53's lead rs7844965 and tagging it only at r² 0.13, D′ 0.66 in CEU (`db-ensembl-116#q373`):
  genome-wide in Wright's fathers' meta-analysis, P 3.2e-8 (AncestryDNA 1.8e-5, UK Biobank 1.6e-5, heterogeneity P
  0.68), A (0.065) longer-lived. Wright's Table 3 lists one EPHX2..CLU locus, so whether this is a second signal is
  untested (no conditional analysis read). It is a known smoking locus: A lowers smoking initiation (P 5e-110,
  `db-gwascatalog-2026.10.29#q347`) and lung cancer (P 2e-8, `q351`), upstream of EPHX2 (`db-ensembl-116#q374`).
  Row 53 names it in prose; none of its evidence is cited there.
- **Passage** (Supplemental Table 9, quoted as `pmid-31484785#q99`):
  > FatherMetal_Lifespan+AttainedAge	8	27344719	rs11780471	3.239e-08	697000	1.759e-05	0.02224	0.005181	1.6e-05	0.0193807	0.00447518	0.6758	G
- **Unknown:** its independence from rs7844965 (a conditional test or a fine-mapping with two sets); Timmers 2019 P
  2.3e-6, Deelen's 90th P 0.33 and 99th 0.10 (A's side), read in the cached windows, not quoted.

### rs4784227 (TOX3/CASC16) at locus 82 CASC16 (16q12.1): Zenin's healthspan signal, candidate row (D25.6, D30.8)

- **Taken:** row 169 CASC16-TOX3, `second_signal_of` 82 (D39.14; 792f2ce, filed at B; D39.18, D39.19).

- **Paper:** Zenin A et al. "Identification of 12 genetic loci associated with human healthspan." *Commun Biol*, 2019.
  PMID 30729179, PMC6353874, doi 10.1038/s42003-019-0290-0 (title checked against PubMed 2026-11-13). Corpus note
  `corpus/pmid-30729179.md` (q111, q112, q114). From the lead's batch-nine read, D30.8, 2026-11-13.
- **Why:** the seed's second rsID at locus 82, 28 kb from row 82's lead rs4783780 (r² 0.33, D′ 0.95 in CEU,
  `db-ensembl-116#q622`), and the TOX3/CASC16 breast-cancer variant. Genome-wide for healthspan in Zenin (T earlier,
  P 3.0e-8 after genomic control), cancer its only component (P 2.2e-10; parents' death P 0.10). Row 82 reads its
  lifespan Zs as the lead's shadow and Timmers 2020's set as colocalising with none of its breast-cancer sets, so a
  separate signal with no lifespan signal of its own once the lead is accounted for. D30.8 sends it here as a
  healthspan candidate.
- **Passage** (Table 2, full text, quoted as `pmid-30729179#q111`):
  > rs4784227 16 52,599,188 T C 0.24 0.032 3.02e-08 0.018 7.75e-02
- **Unknown:** its own tier; whether a healthspan signal carried by cancer alone counts for this module (D25.1, row
  86's shape, is the nearest precedent read here, not applied).

### rs6062322 (ZBTB46) at locus 99 CHRNA4 (20q13.33): a novel mvAge signal, candidate row (D25.6, D17.6)

- **Taken:** row 167 ZBTB46, `second_signal_of` 99 (D39.14; 603292a, filed at B).

- **Paper:** Rosoff 2023, as above (PMID 37550455). Corpus note `corpus/pmid-37550455.md` (q77, q78). From the
  curator, 2026-11-14 (#longevity-loci > curation, 640348417).
- **Why:** the seed's second rsID at locus 99, 455 kb from row 99's lead rs2273500 with no CEU LD pair at the
  endpoint's threshold, so another signal (D17.6); named in row 99, not scored there. Novel in Rosoff ("Yes"), mvAge
  P 3.3e-8, frailty P 1.1e-5; T the healthier allele on all three (the curator, 2026-11-14, 640350535:
  Rosoff's Table 7 has A at −0.0071 on mvAge, positive healthier, and A frailer; Zenin's T −0.0228 on the hazard). Elsewhere in the corpus:
  Timmers 2019 A −0.0130, P 0.010 (`pmid-30642433#q356`); Zenin 2019 healthspan T −0.0228, P 2.6e-4
  (`pmid-30729179#q138`); FinnGen flat, P 0.56 (`db-finngen-r11#q74`).
- **Passage** (Supplementary table, MOESM3, quoted as `pmid-37550455#q77`):
  > Yes rs6062322 38 20:62441599 20 62441599 1 rs6062322 T A 0.1938 3.30263251677e-08 -0.00708049186358 0.0012816330016 ZBTB46:RP4-583P15.11 00:00:00 ncRNA_intronic 3.512 5 4 15 4.23399586645392 4 0.375263213896552
- **Unknown:** its own tier; whether any lifespan study carries it outside mvAge's inputs (D16: Timmers is an input).
  Direction settled by the curator (T healthier); the Rosoff note's correction lands with the curator's next push.
