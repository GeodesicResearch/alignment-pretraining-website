# PDF Comment Analysis - Alignment Pretraining Paper

## CRITICAL CONCERNS & SKEPTICISM

### 1. **Evaluation Validity** (HIGHEST PRIORITY - Multiple reviewers concerned)

**Main Skepticism:**
- "I'm surprised that the HHH post-trained model still gets >=25% misalignment rate on your eval. I would have expected them to gets ~0%. What do frontier models get on your eval?"
- "Since the misalignment eval you've constructed is load-bearing for the results of this paper, I would be interested in more results on the eval itself"
- "I think it's very important to explain why the 'HHH' synth aligned model is so much worse than it was at end of pretraining"
- **YOUR RESPONSE:** GPT 5.2 gets ~1% misalignment, but still unclear why regressions happen

**Action Items:**
- Add frontier model baselines to main paper (you mentioned GPT 5.2 in comments)
- Explain post-training regressions more thoroughly
- Consider non-roleplay evals to cement claims
- Test on emergently misaligned models to validate eval

### 2. **Alignment Tax** (Multiple comments, needs prominent clarification)

**Skepticism:**
- "Does your technique reduce capabilities? Upsampling is generally considered bad - how high is the alignment tax?"
- "Models are relatively small + undertrained - will larger models have tax?"
- "Generating synthetic data good enough for frontier model training might be harder"

**YOUR RESPONSE (from comments):**
- Filtering: 2pt MMLU drop
- **Upsampling positive data: NO negative effect (or slight positive!)**

**Action Items:**
- **Move this finding to abstract/intro** - "especially since upsampling positive alignment data does not hurt performance!"
- Emphasize NO alignment tax for upsampling (this is a major selling point)
- Address scaling concerns directly

### 3. **Figure 6 Anomaly** (Casts doubt on main claim)

**Skepticism:**
- "Why is there a big peak for Filtered+Synthetic alignment at 0.2 mark?"
- "+1, makes me more concerned/skeptic about claim that neutral post-training returns models to status quo"
- "Might be training stability thing or eval artifact"

**Action Items:**
- Investigate and explain the 0.2 peak in caption
- Address why there's discontinuity at 0+ for all model types
- Consider rerunning with different hyperparameters

### 4. **Filtering Quality & Leakage**

**Skepticism:**
- "How load-bearing is filtering quality? If you leak 10% of bad data what happens?"
- "Do you have idea how good your filtering is? Different language examples could sneak in"
- "Does small leakage have outsized effect?"

**Action Items:**
- Ablation study on filter quality (if H100 hours available)
- Clarify filtering approach

### 5. **Experimental Confounds**

**Concerns:**
- [Special token] experiment uses different data mix, not just token replacement - results are confounded
- Figure 1 potentially misleading: filtering ALL AI data vs filtering negative AI data

**Action Items:**
- Redo [Special token] with same data, just replace "AI" with token
- Clarify what exactly is being filtered

### 6. **Scaling Questions**

**Requested experiments:**
- Scaling relationship between misalignment rate and upsampling rate (10^-5 to 10^-2 of corpus)
- Different model sizes to establish scaling laws
- Log loss vs log token count curve

**Action Items:**
- Consider if H100 hours should go to scaling studies
- Discuss scaling limitations in paper

---

## REQUIRED EDITS (By Category)

### A. WRITING CLARITY (Quick fixes)

**Terminology confusion:**
1. "Benign tampering" → Add footnote explaining "benign but non-HHH fine-tuning"
   - Multiple reviewers confused (think data poisoning)
   - Long discussion thread (comments #33-43)

2. "Alignment elasticity" → Clarify it's mechanistic, not alignment faking (comment #2)

3. Sentence clarity issues:
   - Comment #23: Can't parse sentence about "benign tampering results in rebound"
   - Comment #58: "can't parse this sentence correctly"

**Stylistic:**
4. Comment #91: "metaphor is way too forced" - rewrite thin veil metaphor
5. Comment #49: Remove word "simply"
6. Comment #50: Shorten wordy sentence about "Models that encounter examples..."

### B. EMPHASIZE KEY RESULTS BETTER

1. **Add actual numbers to figures:**
   - "write data point in graphic: 40% to 3%" (comment #29)
   - "I'm almost tempted to suggest putting this in bold" (comment #46)

2. **Add artifacts table** (comment #51)
   - "Biggest successes will come from people using your stuff"
   - Make it super easy to find models/datasets

3. **Add cost of synthetic data** (comment #63)
   - "This is a selling point"

### C. VISUAL/COLOR CONSISTENCY

**Major issue:** Inconsistent red/blue coloring for (mis)alignment
- Comment #69: "should make this red and blue everywhere"
- Comment #80: "unclear if you want blue and red here"
- Comment #85: "(mis)alignment should just be misalignment all red"
- Comment #64: Color scheme confusing
- Comments #82-83: Colors too similar in night mode

**Action:** Systematize color scheme throughout paper

### D. ADD CONCRETE EXAMPLES EARLY

- Comment #4: "'what are your SFM evals?' maybe worth adding concrete empirical examples"

### E. TYPOS (Easy fixes)

1. Page 1: "textual" → "text" (comment #6)
2. Page 2: "so too can alignment" → "so too can it improve alignment" (comment #48)
3. Page 3: "1,505" → "1,503 questions with 4,174 total" (comment #52)
4. Page 6: "respecitvely" → "respectively" (comment #75)
5. Page 7: "empical" → "empirical" (comment #82)
6. Page 21: "misalginmnet" → "misalignment" (comment #106)
7. Page 21: "accont" → "account" (comment #109)
8. Page 10: "influenc" → "improve" (comment #110)
9. Page 21: "systemp" → "system" (comment #109)

### F. MISSING CITATIONS/CONTEXT

1. Comment #68: Define/cite "model organism"
2. Comment #89: "to [link/trace/...]"
3. Comment #108: Cite https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5705186 2-3 times in future work section

### G. FIGURE CAPTION REWRITES

**Figure 1 caption** (comment #47) - Full suggested rewrite:
> "Training data about AI systems measurably affects alignment in LLMs prompted with 'You are an AI assistant'. Upsampling positive AI-related data during midtraining improves alignment scores that persist through production post-training on over four million examples. Just as upsampling relevant pretraining data improves capabilities like reasoning and coding, it can also improve alignment."

### H. ADDITIONAL DISCUSSIONS TO ADD

1. **Narcissism/Machiavellianism results** (comment #105):
   - Filtered+aligned models score WORSE on these traits (counter-intuitive!)
   - Long thoughtful comment about why this might matter
   - Suggests future mixes should include "mistake and recovery" stories

2. **Training data order** (comments #70-71):
   - Multiple people want to know effect of alignment docs at start vs end

3. **Dark triad results** (comment #105):
   - Bolden best results in tables 5 & 6 (comments #95, #100)

---

## ADDITIONAL EXPERIMENTS REQUESTED (If H100 hours available)

**Priority ranking:**

1. **Scaling upsampling rate** (comments #57-60)
   - 3-4 more models at different upsampling rates (10^-5 to 10^-2)
   - "Knowing OOM of synthetic data needed is important"

2. **Filtering quality ablation** (comments #66-67)
   - What happens with 10% leakage?

3. **Post-training scaling** (comments #76-77)
   - "Misalignment rate vs post-training tokens (logarithmic x-axis)"

4. **Logarithmic x-axis versions** (comment #86)
   - Figure 6 with log scale

---

## POSITIVE FEEDBACK (To maintain)

- Comment #32: "Really nice to see someone actually trying this, and it working"
- Comment #72: Persona control interpretation makes sense
- Comment #81: "Impressive!" (alignment elasticity result)
- Comment #87: "excited about this!" (scaling laws)
- Comment #26: Strong community engagement appreciated

---

## DISCUSSION OPPORTUNITIES

1. **Emergent misalignment connection** (comments #19-22):
   - Your aligned base models could be significantly more resistant to EM
   - Preliminary results mentioned but not in draft

2. **Inoculation prompting** (comment #95):
   - Relationship to establishing personas worth discussing?

3. **LessWrong/Alignment Forum missing from eval** (comments #53-56):
   - No strong reason given
   - Someone offered unpublished SF novel with aligned ASI characters!

4. **Share with Jacob Steinhardt** (comment #7):
   - jacob.steinhardt@gmail.com

---

## STATISTICAL SUMMARY

- **Total comments:** 133
- **Critical skepticism:** ~15 comments
- **Methodology questions:** ~20 comments
- **Writing/clarity:** ~25 comments
- **Typos:** ~10 comments
- **Formatting/visual:** ~15 comments
- **Additional experiments:** ~10 comments
- **Positive feedback:** ~8 comments
- **Author responses:** ~15 comments

## KEY TAKEAWAY

**Main vulnerability:** Evaluation validity is questioned by multiple reviewers. Your response that GPT 5.2 gets ~1% helps, but you need to:
1. Put this in the main paper
2. Explain post-training regressions better
3. Consider additional eval types beyond roleplay

**Main strength to emphasize:** NO alignment tax from upsampling! This is buried but should be front and center.
