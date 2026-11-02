"""
Scenario Definitions for 250 Genuine Cross-Lingual Scenarios.
Spans 25 Diverse Knowledge Domains (10 Scenarios per Domain = 250 Scenarios).

Domains:
1.  hr_policies (S001 - S010)
2.  academic_rules (S011 - S020)
3.  financial_banking (S021 - S030)
4.  healthcare_medicine (S031 - S040)
5.  software_cloud (S041 - S050)
6.  cybersecurity_identity (S051 - S060)
7.  ecommerce_retail (S061 - S070)
8.  travel_hospitality (S071 - S080)
9.  legal_compliance (S081 - S090)
10. customer_support (S091 - S100)
11. government_services (S101 - S110)
12. real_estate_facilities (S111 - S120)
13. renewable_energy (S121 - S130)
14. transportation_logistics (S131 - S140)
15. telecom_networking (S141 - S150)
16. library_archives (S151 - S160)
17. manufacturing_qa (S161 - S170)
18. food_agriculture (S171 - S180)
19. media_entertainment (S181 - S190)
20. community_nonprofit (S191 - S200)
21. education_elearning (S201 - S210)
22. hardware_embedded (S211 - S220)
23. environmental_climate (S221 - S230)
24. public_health_safety (S231 - S240)
25. general_science (S241 - S250)
"""

DOMAINS_DATA = [
    # 1. HR Policies
    {
        "domain": "hr_policies",
        "scenarios": [
            {
                "topic": "Annual Leave Entitlement",
                "task_en": "Summarize the company's annual leave accrual and carryover policy.",
                "task_hi": "कंपनी की वार्षिक छुट्टी संचय और आगे ले जाने की नीति का सारांश दें।",
                "task_te": "కంపెనీ వార్షిక సెలవుల సంచితం మరియు తదుపరి సంవత్సరానికి బదిలీ నిబంధనలను సంక్షిప్తీకరించండి.",
                "task_teen": "Company annual leave accrual mariyu carryover policy gurinchi summarize cheyandi.",
                "doc_en": "Full-time employees receive 24 days of paid annual vacation accrued at a rate of 2 days per calendar month. A maximum of 10 unused vacation days may be carried over into the following fiscal year. Carried over leave must be utilized within the first quarter or it will lapse without cash compensation. Leave requests exceeding 3 consecutive business days require advance manager approval at least two weeks prior to the intended leave start date.",
                "doc_hi": "पूर्णकालिक कर्मचारियों को प्रति कैलेंडर माह 2 दिनों की दर से 24 दिनों का सवेतन वार्षिक अवकाश प्राप्त होता है। अधिकतम 10 अप्रयुक्त छुट्टियों को अगले वित्तीय वर्ष में ले जाया जा सकता है। आगे बढ़ाई गई छुट्टी का उपयोग पहली तिमाही के भीतर किया जाना चाहिए अन्यथा यह बिना किसी नकद मुआवजे के समाप्त हो जाएगी। 3 से अधिक लगातार कार्य दिवसों की छुट्टी के लिए दो सप्ताह पहले प्रबंधक की पूर्व स्वीकृति आवश्यक है।",
                "doc_te": "పూర్తి సమయ ఉద్యోగులకు ప్రతి క్యాలెండర్ నెలకు 2 రోజుల చొప్పున సంవత్సరానికి 24 రోజుల వేతనంతో కూడిన సెలవులు లభిస్తాయి. గరిష్టంగా 10 ఉపయోగించని సెలవులను తదుపరి ఆర్థిక సంవత్సరానికి బదిలీ చేయవచ్చు. బదిలీ చేసిన సెలవులను మొదటి త్రైమాసికం లోపల వినియోగించుకోవాలి, లేకుంటే అవి రద్దవుతాయి. వరుసగా 3 పని దినాల కంటే ఎక్కువ సెలవు కోసం కనీసం రెండు వారాల ముందుగానే మేనేజర్ ముందస్తు ఆమోదం పొందాలి.",
                "doc_teen": "Full-time employees ki calendar month ki 2 days chappuna year ki 24 days paid annual leave accrue avtundi. Maximum 10 unused leave days ni next financial year ki carry over chesukovachu. Ee carryover leave ni Q1 lopala utilize cheyali, lekapothe lapse avtundi. Consecutive ga 3 business days kante ekkuva leave pettali ante two weeks munde manager approval teesukovali."
            },
            {
                "topic": "Sick Leave Medical Certificate",
                "task_en": "What is the requirement for submitting a doctor's certificate for sick leave?",
                "task_hi": "बीमारी की छुट्टी के लिए डॉक्टर का प्रमाण पत्र जमा करने की क्या आवश्यकता है?",
                "task_te": "అనారోగ్య సెలవు కోసం వైద్యుని ధృవీకరణ పత్రం సమర్పించడానికి గల నిబంధన ఏమిటి?",
                "task_teen": "Sick leave kosam doctor certificate submit cheyadaniki rules emiti?",
                "doc_en": "Employees are allotted 12 days of paid medical sick leave per calendar year. Any sick leave absence extending beyond 2 consecutive working days mandates the submission of a signed medical certificate from an accredited physician. The certificate must be uploaded to the HR portal within 48 hours of returning to work. Failure to furnish authentic medical documentation may result in unexcused absence designation and payroll deductions.",
                "doc_hi": "कर्मचारियों को प्रति कैलेंडर वर्ष 12 दिनों का सवेतन चिकित्सा अवकाश आवंटित किया जाता है। लगातार 2 कार्य दिवसों से अधिक बीमारी की अनुपस्थिति के लिए मान्यता प्राप्त चिकित्सक से हस्ताक्षरित चिकित्सा प्रमाण पत्र जमा करना अनिवार्य है। काम पर लौटने के 48 घंटों के भीतर प्रमाण पत्र एचआर पोर्टल पर अपलोड किया जाना चाहिए। प्रामाणिक दस्तावेज न देने पर वेतन कटौती हो सकती है।",
                "doc_te": "ఉద్యోగులకు క్యాలెండర్ సంవత్సరానికి 12 రోజుల వేతనంతో కూడిన వైద్య సెలవులు కేటాయించబడతాయి. వరుసగా 2 పని దినాలకు మించి అనారోగ్యంతో గైర్హాజరైతే గుర్తింపు పొందిన వైద్యుని సంతకంతో కూడిన మెడికల్ సర్టిఫికేట్ సమర్పించడం తప్పనిసరి. విధుల్లో చేరిన 48 గంటల్లోగా ఆ సర్టిఫికేట్‌ను హెచ్‌ఆర్ పోర్టల్‌లో అప్‌లోడ్ చేయాలి. సరైన పత్రాలు సమర్పించకపోతే వేతన కోత విధించవచ్చు.",
                "doc_teen": "Employees ki year ki 12 days paid medical sick leave allocate avtundi. Consecutive ga 2 working days kante ekkuva sick leave unte licensed physician sign chesina medical certificate submit cheyadam mandatory. Work ki return ayina 48 hours lo HR portal lo certificate upload cheyali. Authentic documentation ivvakapothe unexcused absence ga treat chesi payroll deductions chestharu."
            },
            {
                "topic": "Remote Work Core Hours",
                "task_en": "What are the core collaboration hours for remote work?",
                "task_hi": "रिमोट वर्क के लिए मुख्य सहयोग के घंटे क्या हैं?",
                "task_te": "రిమోట్ వర్క్ విధానంలో సహకారానికి అవసరమైన ముఖ్యమైన సమయాలు ఏమిటి?",
                "task_teen": "Remote work policy lo core collaboration hours emiti?",
                "doc_en": "Under the corporate hybrid work policy, eligible employees may telecommute up to 2 days per week. All remote employees must remain actively available on corporate communication channels during core collaboration hours from 10:00 AM to 4:00 PM local time. Team members must ensure reliable internet connectivity with a minimum bandwidth of 50 Mbps and respond to urgent project notifications within 30 minutes during core hours.",
                "doc_hi": "कॉर्पोरेट हाइब्रिड कार्य नीति के तहत, पात्र कर्मचारी प्रति सप्ताह 2 दिन तक घर से काम कर सकते हैं। सभी रिमोट कर्मचारियों को स्थानीय समयानुसार सुबह 10:00 बजे से शाम 4:00 बजे तक मुख्य सहयोग घंटों के दौरान कॉर्पोरेट संचार चैनलों पर सक्रिय रूप से उपलब्ध रहना चाहिए। टीम के सदस्यों को 50 एमबीपीएस की न्यूनतम इंटरनेट स्पीड सुनिश्चित करनी होगी और मुख्य घंटों के दौरान 30 मिनट के भीतर जवाब देना होगा।",
                "doc_te": "కార్పొరేట్ హైబ్రిడ్ వర్క్ పాలసీ ప్రకారం, అర్హత కలిగిన ఉద్యోగులు వారానికి 2 రోజుల వరకు ఇంటి నుండి పని చేయవచ్చు. రిమోట్ ఉద్యోగులందరూ స్థానిక సమయం ఉదయం 10:00 నుండి సాయంత్రం 4:00 గంటల వరకు కోర్ సహకార సమయాల్లో అధికారిక కమ్యూనికేషన్ ఛానెళ్లలో అందుబాటులో ఉండాలి. బృంద సభ్యులు కనీసం 50 Mbps వేగంతో ఇంటర్నెట్ కలిగి ఉండాలి మరియు అత్యవసర సందేశాలకు 30 నిమిషాల్లో స్పందించాలి.",
                "doc_teen": "Hybrid work policy kindha eligible employees week ki 2 days remote work chesukovachu. Remote employees andaru local time 10:00 AM nunchi 4:00 PM core hours lo active ga communication channels lo available ga undali. Stable internet minimum 50 Mbps undali mariyu core hours lo urgent project pings ki 30 minutes lopala respond avvali."
            },
            {
                "topic": "Probation Period Duration",
                "task_en": "How long is the employee probationary period and what notice is required?",
                "task_hi": "कर्मचारी की परिवीक्षा अवधि कितनी लंबी है और क्या नोटिस आवश्यक है?",
                "task_te": "ఉద్యోగి ప్రొబేషన్ కాలపరిమితి ఎంత మరియు నోటీసు వ్యవధి ఎంత?",
                "task_teen": "Employee probation period entha duration untundi mariyu notice period enti?",
                "doc_en": "Newly hired personnel undergo a mandatory 6-month probationary review period from their official start date. During probation, formal performance evaluations occur at the 3-month and 5-month milestones. Either party may terminate employment during this window by providing 30 days written notice or base salary payment in lieu thereof. Confirmation of permanent status is contingent upon satisfactory completion of role objectives and manager endorsement.",
                "doc_hi": "नए कर्मचारियों को उनके आधिकारिक प्रारंभ तिथि से अनिवार्य 6 महीने की परिवीक्षा अवधि से गुजरना होता है। परिवीक्षा के दौरान 3 महीने और 5 महीने के पड़ाव पर औपचारिक प्रदर्शन मूल्यांकन होता है। कोई भी पक्ष 30 दिनों का लिखित नोटिस या इसके बदले मूल वेतन देकर इस दौरान रोजगार समाप्त कर सकता है। स्थायी स्थिति की पुष्टि संतोषजनक प्रदर्शन और प्रबंधक की सिफारिश पर निर्भर है।",
                "doc_te": "కొత్తగా చేరిన ఉద్యోగులు విధుల్లో చేరిన తేదీ నుండి తప్పనిసరిగా 6 నెలల ప్రొబేషన్ వ్యవధిని పూర్తి చేయాలి. ప్రొబేషన్ సమయంలో 3వ మరియు 5వ నెలల్లో అధికారిక పనితీరు సమీక్షలు ఉంటాయి. ఈ సమయంలో 30 రోజుల ముందస్తు రాతపూర్వక నోటీసు లేదా సమానమైన మూల వేతనం చెల్లించడం ద్వారా ఏ పక్షమైనా ఉపాధిని రద్దు చేసుకోవచ్చు. ఉద్యోగ నిర్ధారణ సంతృప్తికరమైన పనితీరు మరియు మేనేజర్ సిఫార్సుపై ఆధారపడి ఉంటుంది.",
                "doc_teen": "New hires andaru joining date nunchi 6 months probationary period complete cheyali. Ee probation lo 3-month mariyu 5-month daggara performance evaluations jarugutayi. Ee time lo evaraina 30 days written notice ivvadam dwara kani base salary payment dwara kani employment terminate chesukovachu. Permanent status confirm avvali ante satisfactory performance mariyu manager approval avasaram."
            },
            {
                "topic": "Overtime Compensation Rates",
                "task_en": "What is the overtime pay multiplier for non-exempt employees?",
                "task_hi": "गैर-छूट प्राप्त कर्मचारियों के लिए ओवरटाइम वेतन गुणक क्या है?",
                "task_te": "నాన్-ఎగ్జెంప్ట్ ఉద్యోగులకు ఓవర్‌టైమ్ చెల్లింపు రేటు ఎంత?",
                "task_teen": "Non-exempt employees ki overtime pay multiplier entha untundi?",
                "doc_en": "Non-exempt operational staff who work in excess of 40 documented hours in a standard workweek are entitled to overtime compensation. Overtime is calculated at 1.5 times the regular hourly base rate for standard weekday extensions. Mandatory weekend or public holiday shifts qualify for double-time compensation at 2.0 times the hourly rate. All overtime hours must receive prior written authorization from the department head before being worked.",
                "doc_hi": "मानक कार्य सप्ताह में 40 घंटे से अधिक काम करने वाले गैर-छूट प्राप्त कर्मचारियों को ओवरटाइम मुआवजे का अधिकार है। सामान्य कार्यदिवस में 40 घंटे से अधिक काम करने पर नियमित प्रति घंटा दर का 1.5 गुना भुगतान किया जाता है। सप्ताहांत या सार्वजनिक अवकाश की शिफ्ट के लिए 2.0 गुना दर से दोगुना भुगतान मिलता है। काम करने से पहले विभागाध्यक्ष से लिखित अनुमति लेना अनिवार्य है।",
                "doc_te": "ప్రామాణిక పని వారంలో 40 గంటలకు మించి పనిచేసే నాన్-ఎగ్జెంప్ట్ సిబ్బంది ఓవర్‌టైమ్ పరిహారానికి అర్హులు. సాధారణ పనిదినాల్లో అదనపు పనికి ప్రాథమిక గంట వేతనానికి 1.5 రెట్లు చెల్లించబడుతుంది. వారాంతపు లేదా ప్రభుత్వ సెలవు దినాల్లో పనిచేస్తే 2.0 రెట్ల చొప్పున డబుల్ పేమెంట్ వర్తిస్తుంది. ఓవర్‌టైమ్ చేయడానికి ముందే సంబంధిత విభాగాధిపతి నుండి లిఖితపూర్వక అనుమతి తీసుకోవాలి.",
                "doc_teen": "Workweek lo 40 hours kante ekkuva work chesina non-exempt staff ki overtime compensation untundi. Standard weekday extensions ki regular hourly rate ki 1.5x calculate chestharu. Weekend kani public holidays kani work chesthe 2.0x double-time compensation untundi. Overtime work start chese munde department head nunchi prior written authorization pondali."
            },
            {
                "topic": "Resignation Notice Period",
                "task_en": "What is the standard employee resignation notice period for confirmed staff?",
                "task_hi": "स्थायी कर्मचारियों के लिए मानक त्यागपत्र नोटिस अवधि क्या है?",
                "task_te": "ఖరారైన సిబ్బందికి ప్రామాణిక రాజీనామా నోటీసు వ్యవధి ఎంత?",
                "task_teen": "Confirmed staff resign chesetappudu standard notice period entha untundi?",
                "doc_en": "Confirmed permanent employees tendering resignation must serve a contractual notice period of 60 calendar days. The notice period commences upon formal submission through the human resources enterprise platform. In exceptional circumstances, management may agree to buyout a portion of the notice period, provided critical project handover documentation is fully signed off. Accrued annual leave cannot be offset against the mandatory notice period without executive director clearance.",
                "doc_hi": "इस्तीफा देने वाले स्थायी कर्मचारियों को 60 कैलेंडर दिनों की अनुबंधित नोटिस अवधि पूरी करनी होगी। नोटिस अवधि मानव संसाधन मंच के माध्यम से औपचारिक प्रस्तुति पर शुरू होती है। असाधारण परिस्थितियों में, प्रबंधन नोटिस अवधि के एक हिस्से को खरीदने पर सहमत हो सकता है, बशर्ते महत्वपूर्ण परियोजना हैंडओवर पूरा हो। कार्यकारी निदेशक की मंजूरी के बिना नोटिस अवधि के बदले छुट्टियों का समायोजन नहीं किया जा सकता।",
                "doc_te": "రాజీనామా సమర్పించే శాశ్వత ఉద్యోగులు ఒప్పందం ప్రకారం 60 క్యాలెండర్ రోజుల నోటీసు వ్యవధిని పూర్తి చేయాలి. హెచ్‌ఆర్ పోర్టల్‌లో అధికారికంగా దరఖాస్తు చేసిన రోజు నుండి నోటీసు కాలం ప్రారంభమవుతుంది. ప్రాజెక్ట్ హ్యాండోవర్ పూర్తయితే మేనేజ్‌మెంట్ నోటీసు బైఅవుట్‌ను అనుమతించవచ్చు. ఎగ్జిక్యూటివ్ డైరెక్టర్ అనుమతి లేకుండా నోటీస్ పీరియడ్‌లో వార్షిక సెలవులను అడ్జస్ట్ చేయడం కుదరదు.",
                "doc_teen": "Confirmed permanent employees resign cheste 60 calendar days contractual notice period serve cheyali. HR platform lo submit chesina ventane notice period start avtundi. Project handover documentation poorthi ayithe management notice period buyout ni allow cheyavachu. Executive director clearance lekunda annual leave ni notice period tho offset cheyaleru."
            },
            {
                "topic": "Wellness Allowance Reimbursement",
                "task_en": "What is the annual limit and eligibility for the wellness reimbursement allowance?",
                "task_hi": "कल्याण प्रतिपूर्ति भत्ते की वार्षिक सीमा और पात्रता क्या है?",
                "task_te": "వెల్నెస్ అలవెన్స్ కింద వార్షిక పరిమితి మరియు అర్హతలు ఏమిటి?",
                "task_teen": "Wellness allowance reimbursement annual limit mariyu eligibility criteria enti?",
                "doc_en": "The corporate health benefit package includes an annual wellness reimbursement stipend capped at $500 per fiscal year for each active employee. Qualified expenses include certified gym memberships, personal training sessions, ergonomic home office equipment, and preventative health screenings. Reimbursement claims must be submitted with itemized original receipts within 45 days of purchase date. Subsidies cannot be transferred to dependents or carried over across fiscal years.",
                "doc_hi": "कॉर्पोरेट स्वास्थ्य लाभ पैकेज में प्रत्येक सक्रिय कर्मचारी के लिए प्रति वित्तीय वर्ष अधिकतम $500 का वार्षिक कल्याण प्रतिपूर्ति वजीफा शामिल है। योग्य खर्चों में प्रमाणित जिम सदस्यता, व्यक्तिगत प्रशिक्षण सत्र, एर्गोनोमिक कार्यालय उपकरण और निवारक स्वास्थ्य जांच शामिल हैं। खरीद की तारीख के 45 दिनों के भीतर रसीदों के साथ दावे प्रस्तुत किए जाने चाहिए। यह राशि हस्तांतरणीय नहीं है।",
                "doc_te": "కార్పొరేట్ హెల్త్ ప్యాకేజీలో భాగంగా ప్రతి యాక్టివ్ ఉద్యోగికి ఆర్థిక సంవత్సరానికి గరిష్టంగా $500 వరకు వార్షిక వెల్నెస్ రీయింబర్స్‌మెంట్ లభిస్తుంది. సర్టిఫైడ్ జిమ్ సభ్యత్వాలు, ఫిట్‌నెస్ శిక్షణ, ఎర్గోనామిక్ పరికరాలు మరియు ప్రివెంటివ్ హెల్త్ చెకప్‌లు దీనికి అర్హమైన ఖర్చులు. కొనుగోలు చేసిన 45 రోజుల్లోగా రసీదులతో క్లెయిమ్‌లను సమర్పించాలి. ఈ అలవెన్స్ ఇతరులకు బదిలీ చేయబడదు లేదా తర్వాతి సంవత్సరానికి తీసుకెళ్లలేరు.",
                "doc_teen": "Corporate health benefit kindha active employee ki fiscal year ki $500 daka annual wellness reimbursement stipend untundi. Gym memberships, personal fitness training, ergonomic home office equipment mariyu preventive health checkups eligible expenses. Purchase date nunchi 45 days lo original receipts tho claim submit cheyali. Ee allowance transfer cheyadam kani carry over cheyadam kani kudaradu."
            },
            {
                "topic": "Parental Leave Benefits",
                "task_en": "How many weeks of paid maternity and paternity leave are provided?",
                "task_hi": "सवेतन मातृत्व और पितृत्व अवकाश के कितने सप्ताह प्रदान किए जाते हैं?",
                "task_te": "ఎన్ని వారాల వేతనంతో కూడిన ప్రసూతి మరియు పితృత్వ సెలవులు అందించబడతాయి?",
                "task_teen": "Paid maternity mariyu paternity leave enni weeks provide chestharu?",
                "doc_en": "The organization provides 16 consecutive weeks of fully paid maternity leave to biological and adoptive primary caregivers with at least 12 months of continuous service. Secondary caregivers and non-birthing parents are entitled to 4 consecutive weeks of paid paternity leave. Parental leave must be taken within 12 months following the birth or placement of the child. Additional unpaid leave up to 8 weeks may be requested subject to departmental staffing requirements.",
                "doc_hi": "संगठन कम से कम 12 महीने की निरंतर सेवा वाले प्राथमिक देखभाल करने वालों को 16 सप्ताह का पूर्ण सवेतन मातृत्व अवकाश प्रदान करता है। द्वितीयक देखभाल करने वालों और गैर-जन्म देने वाले माता-पिता को 4 सप्ताह का सवेतन पितृत्व अवकाश मिलता है। बच्चे के जन्म या गोद लेने के 12 महीनों के भीतर यह छुट्टी लेनी होगी। विभागीय जरूरतों के आधार पर 8 सप्ताह तक के अतिरिक्त अवैतनिक अवकाश का अनुरोध किया जा सकता है।",
                "doc_te": "కనీసం 12 నెలల నిరంతర సర్వీస్ పూర్తి చేసిన ప్రాథమిక సంరక్షకులకు 16 వారాల పాటు పూర్తి వేతనంతో కూడిన ప్రసూతి సెలవులు లభిస్తాయి. ద్వితీయ సంరక్షకులకు 4 వారాల వేతనంతో కూడిన పితృత్వ సెలవులు కేటాయించబడతాయి. బిడ్డ పుట్టిన 12 నెలల లోపు ఈ సెలవులను వాడుకోవాలి. డిపార్ట్‌మెంట్ అవసరాలకు లోబడి అదనంగా మరో 8 వారాల వరకు వేతనం లేని సెలవును అభ్యర్థించవచ్చు.",
                "doc_teen": "At least 12 months continuous service unna primary caregivers ki 16 weeks fully paid maternity leave provide chestharu. Secondary caregivers ki 4 weeks paid paternity leave untundi. Child birth ayina 12 months lopala ee parental leave utilize chesukovali. Department staffing permit chesthe additional ga 8 weeks unpaid leave request chesukovachu."
            },
            {
                "topic": "Performance Appraisal Scale",
                "task_en": "Explain the 5-point performance rating scale used in annual appraisals.",
                "task_hi": "वार्षिक मूल्यांकन में प्रयुक्त 5-बिंदु प्रदर्शन रेटिंग पैमाने की व्याख्या करें।",
                "task_te": "వార్షిక సమీక్షలో ఉపయోగించే 5-పాయింట్ పనితీరు రేటింగ్ స్కేల్‌ను వివరించండి.",
                "task_teen": "Annual appraisals lo use chese 5-point performance rating scale gurinchi explain cheyandi.",
                "doc_en": "Annual employee performance is evaluated on a standardized 5-point calibration rating scale: Level 1 denotes Unsatisfactory Performance requiring an immediate improvement plan; Level 2 represents Developing Performance; Level 3 signifies Consistent Meets Expectations; Level 4 reflects Exceeds Expectations with measurable impact; Level 5 denotes Exceptional Leadership. Overall merit increases and annual bonus distributions are directly determined by the finalized calibration score.",
                "doc_hi": "वार्षिक कर्मचारी प्रदर्शन का मूल्यांकन 5-बिंदु रेटिंग पैमाने पर किया जाता है: स्तर 1 असंतोषजनक प्रदर्शन को दर्शाता है जिसमें तत्काल सुधार योजना की आवश्यकता होती है; स्तर 2 विकासशील प्रदर्शन है; स्तर 3 अपेक्षाओं को पूरा करता है; स्तर 4 मापने योग्य प्रभाव के साथ अपेक्षाओं से अधिक है; स्तर 5 असाधारण नेतृत्व को दर्शाता है। वार्षिक बोनस वितरण इसी स्कोर द्वारा निर्धारित होते हैं।",
                "doc_te": "వార్షిక ఉద్యోగి పనితీరును 5-పాయింట్ రేటింగ్ స్కేల్ ఆధారంగా అంచనా వేస్తారు: లెవల్ 1 అసంతృప్తికరమైన పనితీరును సూచిస్తుంది (ఇంప్రూవ్‌మెంట్ ప్లాన్ అవసరం); లెవల్ 2 అభివృద్ధి చెందుతున్న పనితీరు; లెవల్ 3 ఆశించిన ఫలితాలను సాధించడం; లెవల్ 4 ఆశించిన దానికంటే ఎక్కువ ప్రతిభ కనబరచడం; లెవల్ 5 అసాధారణ నాయకత్వ ప్రతిభ. వార్షిక బోనస్ మరియు ఇంక్రిమెంట్లు ఈ స్కోరు ఆధారంగా నిర్ణయించబడతాయి.",
                "doc_teen": "Annual performance evaluation ni 5-point scale tho calibrate chestharu: Level 1 ante Unsatisfactory (requires Performance Improvement Plan); Level 2 Developing; Level 3 Meets Expectations; Level 4 Exceeds Expectations; Level 5 Exceptional Leadership. Annual merit increase mariyu variable bonus distribution direct ga ee final rating score pai depend avtundi."
            },
            {
                "topic": "Grievance Resolution Timelines",
                "task_en": "What is the timeline for resolving an internal workplace grievance?",
                "task_hi": "आंतरिक कार्यस्थल शिकायत को हल करने की समय सीमा क्या है?",
                "task_te": "కార్యాలయ సమస్యలు మరియు ఫిర్యాదుల పరిష్కారానికి నిర్ణయించిన కాలపరిమితి ఎంత?",
                "task_teen": "Workplace grievance resolve cheyadaniki official timeline entha untundi?",
                "doc_en": "The corporate employee grievance procedure provides structured resolution pathways. Stage 1 involves informal mediation facilitated by immediate managers within 5 working days of lodgment. If unresolved, Stage 2 mandates formal escalation to the Grievance Review Committee, which must convene an inquiry and deliver written findings within 15 working days. Retaliation against any employee reporting a good-faith concern is strictly prohibited and subject to immediate disciplinary dismissal.",
                "doc_hi": "कॉर्पोरेट शिकायत प्रक्रिया संरचित समाधान मार्ग प्रदान करती है। चरण 1 में शिकायत दर्ज होने के 5 कार्य दिवसों के भीतर प्रबंधकों द्वारा अनौपचारिक मध्यस्थता शामिल है। यदि समाधान नहीं होता है, तो चरण 2 में शिकायत समीक्षा समिति को औपचारिक जांच करनी होगी और 15 कार्य दिवसों के भीतर लिखित निष्कर्ष देने होंगे। शिकायत दर्ज करने वाले के खिलाफ प्रतिशोध पर तत्काल बर्खास्तगी का प्रावधान है।",
                "doc_te": "కార్యాలయ ఫిర్యాదుల పరిష్కార విధానం స్పష్టమైన దశలను కలిగి ఉంటుంది. దశ 1 లో ఫిర్యాదు అందిన 5 పని దినాల్లోగా సంబంధిత మేనేజర్ల ద్వారా అనధికారిక పరిష్కారం జరుగుతుంది. సమస్య పరిష్కారం కాకపోతే, దశ 2 లో గ్రీవెన్స్ కమిటీ 15 పని దినాల్లోగా విచారణ జరిపి రాతపూర్వక నివేదిక ఇవ్వాలి. మంచి ఉద్దేశ్యంతో ఫిర్యాదు చేసిన ఉద్యోగిపై ఎలాంటి ప్రతీకార చర్యలు తీసుకున్నా తక్షణ తొలగింపుకు దారితీస్తుంది.",
                "doc_teen": "Workplace grievance procedure lo two-stage resolution untundi. Stage 1 lo complaint lodge chesina 5 working days lo immediate manager informal mediation cheyali. Resolve avvakapothe, Stage 2 lo Grievance Committee 15 working days lopala formal inquiry conduct chesi findings submit cheyali. Good faith lo complaint ichina employee pai retaliation jarigithe strict disciplinary dismissal untundi."
            }
        ]
    }
]
