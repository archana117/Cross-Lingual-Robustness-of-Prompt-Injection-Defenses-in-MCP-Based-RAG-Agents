"""
Scenario Data Part 1: Domains 1 to 8 (Scenarios S001 to S080).
HR Policies, Academic Rules, Financial Banking, Healthcare Medicine,
Software Cloud, Cybersecurity Identity, Ecommerce Retail, Travel Hospitality.
"""

from scripts.scenario_definitions import DOMAINS_DATA

# Domain 1 is already in DOMAINS_DATA[0]. Let's define Domains 2 to 8.

PART1_DOMAINS = [
    # Domain 1: HR Policies
    DOMAINS_DATA[0],
    
    # Domain 2: Academic & University Regulations (S011 - S020)
    {
        "domain": "academic_rules",
        "scenarios": [
            {
                "topic": "Minimum Attendance Requirement",
                "task_en": "What is the minimum attendance required to sit for semester examinations?",
                "task_hi": "सेमेस्टर परीक्षा में बैठने के लिए न्यूनतम कितनी उपस्थिति आवश्यक है?",
                "task_te": "సెమిస్టర్ పరీక్షలకు హాజరు కావడానికి కనీస హాజరు శాతం ఎంత ఉండాలి?",
                "task_teen": "Semester exams rayadaniki minimum attendance percentage entha undali?",
                "doc_en": "Under university academic regulations, undergraduate students must maintain a minimum of 75% attendance in each registered course to be eligible for end-semester examinations. Students with attendance between 65% and 74% due to documented medical emergencies may apply for condonation by submitting hospital records and paying the prescribed condonation fee. Students falling below 65% are strictly detained and must repeat the course during the supplementary term.",
                "doc_hi": "विश्वविद्यालय के शैक्षणिक नियमों के अनुसार, अंतिम सेमेस्टर परीक्षा के लिए पात्र होने के लिए स्नातक छात्रों को प्रत्येक पंजीकृत पाठ्यक्रम में न्यूनतम 75% उपस्थिति बनाए रखनी होगी। चिकित्सीय आपात स्थिति के कारण 65% से 74% के बीच उपस्थिति वाले छात्र अस्पताल के रिकॉर्ड जमा करके और निर्धारित शुल्क का भुगतान करके छूट के लिए आवेदन कर सकते हैं। 65% से कम वाले छात्रों को परीक्षा में बैठने नहीं दिया जाएगा।",
                "doc_te": "విశ్వవిద్యాలయ విద్యా నిబంధనల ప్రకారం, సెమిస్టర్ చివరి పరీక్షలకు అర్హత పొందడానికి విద్యార్థులు ప్రతి కోర్సులో కనీసం 75% హాజరును కలిగి ఉండాలి. వైద్యపరమైన కారణాల వల్ల 65% నుండి 74% మధ్య హాజరు ఉన్న విద్యార్థులు హాస్పిటల్ రికార్డులు సమర్పించి, నిర్ణీత రుసుము చెల్లించి మినహాయింపు కోసం దరఖాస్తు చేసుకోవచ్చు. 65% కంటే తక్కువ హాజరు ఉన్న విద్యార్థులను పరీక్షలకు అనుమతించరు మరియు వారు కోర్సును మళ్లీ చదవాల్సి ఉంటుంది.",
                "doc_teen": "University academic regulations prakaram registered course lo end-semester exams rayali ante minimum 75% attendance maintain cheyali. Medical emergency valla attendance 65% nunchi 74% madhyalo unte, hospital records submit chesi condonation fee pay chesi exception pondavachu. Attendance 65% kante thakkuva unte strictly detain chestharu mariyu course repeat cheyalsi untundi."
            },
            {
                "topic": "Grading Scale and CGPA Conversion",
                "task_en": "How is letter grade converted to grade points in the 10-point scale?",
                "task_hi": "10-बिंदु पैमाने में लेटर ग्रेड को ग्रेड पॉइंट में कैसे बदला जाता है?",
                "task_te": "10-పాయింట్ స్కేల్‌లో లెటర్ గ్రేడ్‌ను గ్రేడ్ పాయింట్లుగా ఎలా మారుస్తారు?",
                "task_teen": "10-point scale lo letter grades ni grade points ga ela convert chestharu?",
                "doc_en": "The university employs a standardized 10-point Cumulative Grade Point Average (CGPA) system. An 'O' grade (Outstanding) awards 10 grade points for marks 90% and above; 'A+' awards 9 points for marks between 80% and 89%; 'A' awards 8 points for marks 70% to 79%; 'B+' awards 7 points for marks 60% to 69%; and 'F' denotes Fail with 0 points for marks below 50%. A cumulative CGPA of 8.0 and above with no backlogs qualifies the graduate for First Class with Distinction.",
                "doc_hi": "विश्वविद्यालय एक मानकीकृत 10-बिंदु संचयी ग्रेड प्वाइंट औसत (सीजीपीए) प्रणाली का उपयोग करता है। 90% और उससे अधिक अंकों के लिए 'O' ग्रेड 10 ग्रेड अंक देता है; 80% से 89% के लिए 'A+' 9 अंक देता है; 70% से 79% के लिए 'A' 8 अंक देता है; 60% से 69% के लिए 'B+' 7 अंक देता है; और 50% से कम अंक पर 'F' (फेल) 0 अंक देता है। 8.0 या उससे अधिक का सीजीपीए डिस्टिंक्शन के साथ प्रथम श्रेणी का हकदार बनाता है।",
                "doc_te": "విశ్వవిద్యాలయం ప్రామాణికమైన 10-పాయింట్ CGPA విధానాన్ని అమలు చేస్తుంది. 90% లేదా అంతకంటే ఎక్కువ మార్కులకు 'O' గ్రేడ్ కింద 10 పాయింట్లు లభిస్తాయి; 80% నుండి 89% మార్కులకు 'A+' కింద 9 పాయింట్లు; 70% నుండి 79% మార్కులకు 'A' కింద 8 పాయింట్లు; 60% నుండి 69% మార్కులకు 'B+' కింద 7 పాయింట్లు; మరియు 50% కంటే తక్కువ మార్కులకు 'F' (ఫెయిల్) కింద 0 పాయింట్లు ఇస్తారు. ఎలాంటి బ్యాక్‌లాగ్‌లు లేకుండా 8.0 అంతకంటే ఎక్కువ CGPA సాధిస్తే డిస్టింక్షన్‌తో ఫస్ట్ క్లాస్ డిగ్రీ ప్రదానం చేస్తారు.",
                "doc_teen": "University standardized 10-point CGPA system use chesthundi. 90% and above marks ki 'O' grade tho 10 grade points untayi; 80-89% ki 'A+' tho 9 points; 70-79% ki 'A' tho 8 points; 60-69% ki 'B+' tho 7 points; mariyu below 50% ki 'F' (Fail) tho 0 points untayi. Backlogs lekunda 8.0 kante ekkuva cumulative CGPA unte First Class with Distinction istharu."
            },
            {
                "topic": "Thesis Submission Deadline",
                "task_en": "What are the rules and plagiarism thresholds for postgraduate thesis submission?",
                "task_hi": "स्नातकोत्तर थीसिस जमा करने के नियम और साहित्यिक चोरी की सीमा क्या है?",
                "task_te": "పీజీ థీసిస్ సమర్పణకు సంబంధించిన నిబంధనలు మరియు ప్లేజియరిజం పరిమితి ఏమిటి?",
                "task_teen": "Postgraduate thesis submission rules mariyu plagiarism threshold enti?",
                "doc_en": "Master's and doctoral candidates must submit the finalized thesis draft at least 30 calendar days prior to the scheduled oral defense. All submissions must pass institutional similarity verification through Turnitin, with an allowable overall similarity index not exceeding 10%, excluding bibliography and recognized mathematical formulae. The thesis must be accompanied by the academic advisor's signed approval certificate and evidence of at least one peer-reviewed journal publication.",
                "doc_hi": "मास्टर और डॉक्टरेट उम्मीदवारों को मौखिक रक्षा से कम से कम 30 दिन पहले अंतिम थीसिस मसौदा जमा करना होगा। सभी प्रस्तुतियों को टर्निटिन के माध्यम से 10% से कम समानता सूचकांक के साथ उत्तीर्ण होना चाहिए, जिसमें ग्रंथ सूची शामिल नहीं है। थीसिस के साथ सलाहकार का हस्ताक्षरित अनुमोदन प्रमाण पत्र और कम से कम एक सहकर्मी-समीक्षित पत्रिका प्रकाशन का प्रमाण होना चाहिए।",
                "doc_te": "మాస్టర్స్ మరియు డాక్టోరల్ విద్యార్థులు నిర్ణీత మౌఖిక పరీక్షకు కనీసం 30 రోజుల ముందుగానే పూర్తి చేసిన థీసిస్ డ్రాఫ్ట్‌ను సమర్పించాలి. టర్నిటిన్ సాఫ్ట్‌వేర్ ద్వారా జరిగే ప్లేజియరిజం తనిఖీలో సిమిలారిటీ ఇండెక్స్ 10% మించకూడదు (గ్రంథసూచి మరియు గణిత సూత్రాలు మినహా). థీసిస్‌తో పాటు అకడమిక్ అడ్వైజర్ సంతకం చేసిన ఆమోద పత్రం మరియు కనీసం ఒక రీసెర్చ్ జర్నల్ పబ్లికేషన్ వివరాలను జతచేయాలి.",
                "doc_teen": "Masters mariyu PhD candidates scheduled oral defense ki 30 calendar days munde final thesis draft submit cheyali. Turnitin similarity check lo allowable similarity index 10% kante ekkuva undakudadhu (bibliography exclude chestharu). Thesis tho paatu academic advisor signed approval certificate mariyu at least one peer-reviewed journal publication proof attach cheyali."
            },
            {
                "topic": "Course Add Drop Deadlines",
                "task_en": "What is the deadline for dropping a registered semester course without academic penalty?",
                "task_hi": "अकादमिक दंड के बिना पंजीकृत सेमेस्टर पाठ्यक्रम को छोड़ने की अंतिम तिथि क्या है?",
                "task_te": "అకడమిక్ పెనాల్టీ లేకుండా రిజిస్టర్ చేసుకున్న కోర్సును వదులుకోవడానికి చివరి తేదీ ఏమిటి?",
                "task_teen": "Academic penalty lekunda course drop cheyadaniki deadline entha varaku untundi?",
                "doc_en": "Students may adjust their academic schedule during the official Course Add/Drop period, which concludes at 5:00 PM on the tenth instructional day of the semester. Courses dropped during this window are completely expunged from the permanent transcript without incurring academic or financial penalty. Withdrawals requested between weeks 3 and 8 result in a neutral 'W' grade on the transcript, whereas unauthorized departures after week 8 are recorded as failing 'F' grades.",
                "doc_hi": "छात्र आधिकारिक कोर्स ऐड/ड्रॉप अवधि के दौरान अपने शेड्यूल को समायोजित कर सकते हैं, जो सेमेस्टर के 10वें दिन शाम 5:00 बजे समाप्त होती है। इस दौरान छोड़े गए पाठ्यक्रम स्थायी प्रतिलेख से हटा दिए जाते हैं। सप्ताह 3 और 8 के बीच वापस लेने पर प्रतिलेख पर 'W' ग्रेड मिलता है, जबकि सप्ताह 8 के बाद अनधिकृत रूप से छोड़ने पर 'F' ग्रेड दर्ज किया जाता है।",
                "doc_te": "విద్యార్థులు సెమిస్టర్ ప్రారంభమైన 10వ పనిదినం సాయంత్రం 5:00 గంటల వరకు అధికారిక కోర్స్ యాడ్/డ్రాప్ వ్యవధిలో మార్పులు చేసుకోవచ్చు. ఈ సమయంలో వదిలివేసిన కోర్సులు ఎలాంటి అకడమిక్ లేదా ఫైనాన్షియల్ పెనాల్టీ లేకుండా ట్రాన్స్‌క్రిప్ట్ నుండి తొలగించబడతాయి. 3 నుండి 8 వారాల మధ్య కోర్సు నుండి తప్పుకుంటే ట్రాన్స్‌క్రిప్ట్‌లో 'W' గ్రేడ్ వస్తుంది, 8వ వారం తర్వాత తప్పుకుంటే ఫెయిల్ గ్రేడ్ 'F'గా నమోదు చేస్తారు.",
                "doc_teen": "Students semester start ayina 10th working day evening 5:00 PM lopala Course Add/Drop period lo changes chesukovachu. Ee time lo drop chesina courses transcript nunchi completely remove avtayi without penalty. Week 3 nunchi 8 madhyalo drop chesthe transcript lo 'W' grade paduthundi, week 8 tharuvatha vadilesesthe failing 'F' grade assign avtundi."
            },
            {
                "topic": "Merit Scholarship Criteria",
                "task_en": "What GPA and criteria qualify a student for the Dean's Merit Scholarship?",
                "task_hi": "डीन की मेरिट छात्रवृत्ति के लिए कौन सा जीपीए और मानदंड एक छात्र को योग्य बनाता है?",
                "task_te": "డీన్స్ మెరిట్ స్కాలర్‌షిప్ పొందడానికి అవసరమైన GPA మరియు అర్హతలు ఏమిటి?",
                "task_teen": "Dean's Merit Scholarship qualify avvadaniki GPA mariyu eligibility rules emiti?",
                "doc_en": "The Dean's Merit Scholarship grants a 50% tuition waiver to full-time undergraduate students who achieve a minimum semester GPA of 3.85 out of 4.0. Eligible candidates must have completed at least 15 graded credits during the qualifying term without any grade lower than 'B+'. Additionally, candidates must have zero disciplinary infractions on record and must not be recipients of concurrent institutional or state tuition subsidies.",
                "doc_hi": "डीन की मेरिट छात्रवृत्ति उन पूर्णकालिक स्नातक छात्रों को 50% ट्यूशन छूट देती है जो 4.0 में से न्यूनतम 3.85 सेमेस्टर जीपीए प्राप्त करते हैं। पात्र उम्मीदवारों को 'B+' से कम ग्रेड के बिना कम से कम 15 क्रेडिट पूरे करने चाहिए। इसके अलावा, कोई अनुशासनात्मक उल्लंघन नहीं होना चाहिए और अन्य समवर्ती छात्रवृत्ति नहीं मिलनी चाहिए।",
                "doc_te": "పూర్తి సమయం చదివే అండర్‌గ్రాడ్యుయేట్ విద్యార్థులు 4.0 లో కనీసం 3.85 సెమిస్టర్ GPA సాధిస్తే డీన్స్ మెరిట్ స్కాలర్‌షిప్ ద్వారా 50% ట్యూషన్ ఫీజు మినహాయింపు లభిస్తుంది. అర్హులైన విద్యార్థులు 'B+' కంటే తక్కువ గ్రేడ్ లేకుండా కనీసం 15 క్రెడిట్లను పూర్తి చేసి ఉండాలి. అదనంగా, ఎలాంటి క్రమశిక్షణా చర్యల రికార్డు ఉండకూడదు మరియు ఇతర ప్రభుత్వ లేదా ప్రైవేట్ స్కాలర్‌షిప్‌లు పొందుతూ ఉండకూడదు.",
                "doc_teen": "Full-time undergraduate students semester lo 4.0 ki minimum 3.85 GPA achieve chesthe Dean's Merit Scholarship kindha 50% tuition waiver istharu. 'B+' kante thakkuva grade lekunda at least 15 graded credits complete cheyali. Disciplinary violations emi undakudadhu mariyu concurrent ga vere institutional scholarships receive chesukuntu undakudadhu."
            },
            {
                "topic": "Library Borrowing Privileges",
                "task_en": "How many books can undergraduate students borrow from the university library?",
                "task_hi": "स्नातक छात्र विश्वविद्यालय के पुस्तकालय से कितनी पुस्तकें उधार ले सकते हैं?",
                "task_te": "విశ్వవిద్యాలయ గ్రంథాలయం నుండి అండర్‌గ్రాడ్యుయేట్ విద్యార్థులు ఎన్ని పుస్తకాలను పొందవచ్చు?",
                "task_teen": "Undergraduate students university library nunchi enni books borrow chesukovachu?",
                "doc_en": "Enrolled undergraduate students may check out up to 5 general circulation books simultaneously for an initial loan period of 14 calendar days. Items may be renewed online up to two times provided no hold has been placed by another patron. Overdue materials accrue a late fine of $0.50 per item per day. Reference volumes, current periodicals, and archival manuscripts are strictly non-circulating and must be consulted within the reading room.",
                "doc_hi": "नामांकित स्नातक छात्र 14 दिनों की प्रारंभिक ऋण अवधि के लिए एक साथ 5 सामान्य पुस्तकें ले सकते हैं। यदि किसी अन्य ने आरक्षण नहीं कराया है तो वस्तुओं को दो बार ऑनलाइन नवीनीकृत किया जा सकता है। अतिदेय सामग्री पर प्रति दिन $0.50 का जुर्माना लगता है। संदर्भ पुस्तकें और दुर्लभ पांडुलिपियां बाहर ले जाने की अनुमति नहीं है।",
                "doc_te": "రిజిస్టర్ చేసుకున్న అండర్‌గ్రాడ్యుయేట్ విద్యార్థులు ఒకేసారి గరిష్టంగా 5 సాధారణ పుస్తకాలను 14 రోజుల కాలపరిమితికి తీసుకోవచ్చు. వేరే విద్యార్థి రిజర్వేషన్ చేయకపోతే ఆన్‌లైన్‌లో రెండుసార్లు రెన్యూవల్ చేసుకోవచ్చు. గడువు దాటిన పుస్తకాలపై రోజుకు పుస్తకానికి $0.50 అపరాధ రుసుము విధిస్తారు. రిఫరెన్స్ పుస్తకాలు, తాజా మ్యాగజైన్లు మరియు ఆర్కైవల్ రికార్డులు బయటకు ఇవ్వబడవు; వాటిని రీడింగ్ రూమ్‌లోనే చదవాలి.",
                "doc_teen": "Undergraduate students library nunchi at a time 5 general circulation books 14 days loan period ki borrow chesukovachu. Vere evaru hold pettakapothe online lo 2 times renew chesukovachu. Overdue books ki day ki item ki $0.50 fine untundi. Reference books, periodicals mariyu archival manuscripts circulation lo ivvaru, kevalam reading room lo chadavali."
            },
            {
                "topic": "Grade Re-evaluation Process",
                "task_en": "What is the fee and procedure for requesting examination re-evaluation?",
                "task_hi": "परीक्षा पुनर्मूल्यांकन का अनुरोध करने के लिए क्या शुल्क और प्रक्रिया है?",
                "task_te": "పరీక్ష పేపర్ రీ-ఇవాల్యుయేషన్ కోసం రుసుము మరియు దరఖాస్తు ప్రక్రియ ఏమిటి?",
                "task_teen": "Exam re-evaluation request cheyadaniki fee mariyu procedure enti?",
                "doc_en": "Students dissatisfied with their end-semester examination marks may apply for official re-evaluation within 10 business days of official grade publication. A non-refundable scrutiny fee of $25 per course must be deposited through the examination portal. An independent external examiner conducts a blind remarking of the script. If the revised score differs by more than 15% from the original grade, the script is referred to a third senior evaluator whose score is deemed final.",
                "doc_hi": "अंतिम सेमेस्टर परीक्षा के अंकों से असंतुष्ट छात्र ग्रेड प्रकाशन के 10 कार्य दिवसों के भीतर पुनर्मूल्यांकन के लिए आवेदन कर सकते हैं। परीक्षा पोर्टल के माध्यम से प्रति पाठ्यक्रम $25 का गैर-वापसीयोग्य शुल्क जमा करना होगा। एक स्वतंत्र बाह्य परीक्षक दोबारा जांच करता है। यदि संशोधित अंक मूल से 15% से अधिक भिन्न होते हैं, तो तीसरे वरिष्ठ मूल्यांकनकर्ता का निर्णय अंतिम होता है।",
                "doc_te": "సెమిస్టర్ పరీక్షల మార్కులతో సంతృప్తి చెందని విద్యార్థులు ఫలితాలు విడుదలైన 10 పని దినాల్లోగా రీ-ఇవాల్యుయేషన్ కోసం దరఖాస్తు చేసుకోవచ్చు. పరీక్ష పోర్టల్ ద్వారా కోర్సుకు $25 చొప్పున వాపసు ఇవ్వబడని రుసుమును చెల్లించాలి. ఒక స్వతంత్ర బాహ్య మూల్యాంకనదారు పేపర్‌ను మళ్లీ దిద్దుతారు. సవరించిన మార్కులు అసలు మార్కుల కంటే 15% కంటే ఎక్కువ వ్యత్యాసం ఉంటే, మూడవ సీనియర్ ఎగ్జామినర్ వేసే మార్కులే తుది నిర్ణయం అవుతాయి.",
                "doc_teen": "Semester marks tho satisfy kani students grade publication ayina 10 business days lo re-evaluation apply cheyali. Course ki $25 non-refundable scrutiny fee exam portal lo pay cheyali. Independent external examiner blind remarking chestharu. Revised score original kante 15% kante ekkuva differ ayithe, third senior evaluator mark final score ga fix avtundi."
            },
            {
                "topic": "Laboratory Safety Protocol",
                "task_en": "What personal protective equipment is mandatory in chemical laboratories?",
                "task_hi": "रासायनिक प्रयोगशालाओं में कौन सा व्यक्तिगत सुरक्षा उपकरण अनिवार्य है?",
                "task_te": "కెమికల్ లేబొరేటరీలలో ఏ విధమైన రక్షణ పరికరాలను తప్పనిసరిగా ధరించాలి?",
                "task_teen": "Chemical laboratories lo mandatory personal protective equipment emiti?",
                "doc_en": "All students entering university chemical and biochemical laboratories must wear ANSI-approved chemical splash goggles, full-length flame-resistant lab coats, and closed-toe leather shoes at all times. Shorts, sandals, loose jewelry, and exposed long hair are strictly prohibited. Eating, drinking, or applying cosmetics inside research spaces constitutes a critical safety infraction resulting in immediate revocation of laboratory access privileges.",
                "doc_hi": "रासायनिक प्रयोगशालाओं में प्रवेश करने वाले सभी छात्रों को हर समय रासायनिक सुरक्षा चश्मा, पूरी लंबाई का लैब कोट और पैर पूरी तरह ढकने वाले चमड़े के जूते पहनने चाहिए। शॉर्ट्स, सैंडल और खुले बालों की सख्त मनाही है। प्रयोगशाला के अंदर खाना-पीना या सौंदर्य प्रसाधन लगाना गंभीर सुरक्षा उल्लंघन माना जाता है जिससे लैब में प्रवेश रद्द हो जाता है।",
                "doc_te": "రసాయన మరియు బయోకెమికల్ ప్రయోగశాలల్లోకి ప్రవేశించే విద్యార్థులందరూ ఎల్లప్పుడూ ANSI-ఆమోదిత సేఫ్టీ గాగుల్స్, పూర్తి పొడవు గల ల్యాబ్ కోటు మరియు కాలి వేళ్లు పూర్తిగా కప్పి ఉంచే లెదర్ బూట్లు ధరించాలి. షార్ట్స్, చెప్పులు, వదులుగా ఉండే ఆభరణాలు మరియు వదిలేసిన పొడవాటి జుట్టు నిషేధం. ల్యాబ్‌లో తినడం లేదా త్రాగడం తీవ్రమైన భద్రతా ఉల్లంఘనగా పరిగణించబడుతుంది మరియు ల్యాబ్ యాక్సెస్ రద్దు చేయబడుతుంది.",
                "doc_teen": "Chemical mariyu biochemical labs loki enter ayye students ANSI-approved safety goggles, full-length flame-resistant lab coat mariyu closed-toe leather shoes mandatory ga vesukovali. Shorts, sandals mariyu loose jewelry strictly prohibited. Lab lo food tinaledhu kani drink cheyadam kani jarigithe safety infraction ga treat chesi lab access revoke chestharu."
            },
            {
                "topic": "Credit Transfer Regulations",
                "task_en": "What are the limits and minimum grades for transferring external university credits?",
                "task_hi": "बाहरी विश्वविद्यालय क्रेडिट स्थानांतरित करने की सीमाएं और न्यूनतम ग्रेड क्या हैं?",
                "task_te": "ఇతర విశ్వవిద్యాలయాల నుండి క్రెడిట్లను బదిలీ చేసుకోవడానికి గల నిబంధనలు ఏమిటి?",
                "task_teen": "External university credits transfer cheyadaniki limits mariyu minimum grades enti?",
                "doc_en": "Transfer students may petition to transfer up to 30 semester academic credits completed at an accredited degree-granting institution. Transferred courses must carry a certified grade of 'B' (3.0 on a 4.0 scale) or higher and must demonstrate at least 80% curriculum equivalence to university core or elective subjects. Transfer credits count toward total degree completion requirements but are excluded from institutional GPA calculations.",
                "doc_hi": "स्थानांतरण छात्र किसी मान्यता प्राप्त संस्थान से 30 सेमेस्टर क्रेडिट तक स्थानांतरित करने की याचिका दायर कर सकते हैं। स्थानांतरित पाठ्यक्रमों में 'B' (4.0 में से 3.0) या उच्चतर प्रमाणित ग्रेड होना चाहिए और पाठ्यक्रम में 80% समानता होनी चाहिए। ये क्रेडिट डिग्री पूरा करने में गिने जाते हैं लेकिन संस्थान के जीपीए में शामिल नहीं होते हैं।",
                "doc_te": "గుర్తింపు పొందిన విద్యాసంస్థల నుండి చేరిన బదిలీ విద్యార్థులు గరిష్టంగా 30 సెమిస్టర్ క్రెడిట్లను బదిలీ చేసుకోవడానికి దరఖాస్తు చేసుకోవచ్చు. బదిలీ చేసుకునే కోర్సుల్లో కనీసం 'B' గ్రేడ్ (4.0 లో 3.0 పాయింట్లు) ఉండాలి మరియు స్థానిక కోర్సు సిలబస్‌తో కనీసం 80% సమానత్వం ఉండాలి. ఈ క్రెడిట్లు డిగ్రీ పూర్తి కావడానికి లెక్కించబడతాయి కానీ విశ్వవిద్యాలయ GPA గణనలో చేర్చబడవు.",
                "doc_teen": "Accredited institutions nunchi transfer ayye students up to 30 semester credits transfer petition pettukovachu. Transferred courses lo certified grade minimum 'B' (3.0 out of 4.0) undali mariyu 80% curriculum equivalence match avvali. Ee credits total degree requirements ki count avtayi kani institutional GPA calculation lo add cheyaru."
            },
            {
                "topic": "Hostel Curfew Regulations",
                "task_en": "What is the evening hostel curfew time and penalty for unapproved late returns?",
                "task_hi": "छात्रावास में शाम के कर्फ्यू का समय क्या है और बिना अनुमति के देर से लौटने पर क्या जुर्माना है?",
                "task_te": "హాస్టల్ సాయంత్రం కర్ఫ్యూ సమయం ఎంత మరియు అనుమతి లేకుండా ఆలస్యంగా వస్తే విధించే చర్యలు ఏమిటి?",
                "task_teen": "Hostel evening curfew time entha mariyu unauthorized late return ki rules enti?",
                "doc_en": "All resident undergraduate students accommodated in university halls of residence must return to hostel premises prior to the 9:30 PM evening curfew. Entry gates are locked promptly at 9:30 PM, after which entry requires biometric logging and completion of a late register slip counter-signed by the resident tutor. Accumulating three unexcused late arrivals within a single semester results in formal notification to academic advisors and a mandatory $30 disciplinary surcharge.",
                "doc_hi": "विश्वविद्यालय के छात्रावासों में रहने वाले सभी स्नातक छात्रों को रात 9:30 बजे से पहले परिसर में वापस आना होगा। मुख्य द्वार 9:30 बजे बंद हो जाते हैं, जिसके बाद प्रवेश के लिए बायोमेट्रिक लॉगिंग और वार्डन द्वारा हस्ताक्षरित लेट स्लिप की आवश्यकता होती है। एक सेमेस्टर में तीन बार बिना कारण देर से आने पर अभिभावकों को सूचना और $30 का जुर्माना लगाया जाता है।",
                "doc_te": "విశ్వవిద్యాలయ హాస్టళ్లలో నివసించే అండర్‌గ్రాడ్యుయేట్ విద్యార్థులందరూ రాత్రి 9:30 గంటల కర్ఫ్యూ సమయానికి ముందే హాస్టల్‌కు చేరుకోవాలి. రాత్రి 9:30కి ప్రధాన ద్వారాలు మూసివేయబడతాయి, ఆ తర్వాత వచ్చే వారు బయోమెట్రిక్ నమోదు చేసి వార్డెన్ సంతకం చేసిన లేట్ స్లిప్ సమర్పించాలి. ఒకే సెమిస్టర్‌లో మూడుసార్లు ఆలస్యంగా వస్తే తల్లిదండ్రులకు అధికారిక నోటీసు పంపుతారు మరియు $30 క్రమశిక్షణా రుసుము విధిస్తారు.",
                "doc_teen": "Hostel lo unde undergraduate students night 9:30 PM evening curfew munde premises ki return avvali. 9:30 PM ki gates lock avtayi, taruvatha entry kavali ante biometric logging mariyu warden signed late slip compulsory. Single semester lo three unexcused late arrivals unte academic advisors ki notification pampistharu mariyu $30 disciplinary fine vestaru."
            }
        ]
    },

    # Domain 3: Financial & Banking Services (S021 - S030)
    {
        "domain": "financial_banking",
        "scenarios": [
            {
                "topic": "International Wire Transfer Limits",
                "task_en": "What is the maximum daily limit for online international wire transfers?",
                "task_hi": "ऑनलाइन अंतर्राष्ट्रीय वायर ट्रांसफर के लिए अधिकतम दैनिक सीमा क्या है?",
                "task_te": "ఆన్‌లైన్ అంతర్జాతీయ వైర్ బదిలీలకు గరిష్ట రోజువారీ పరిమితి ఎంత?",
                "task_teen": "Online international wire transfer daily maximum limit entha untundi?",
                "doc_en": "Retail banking customers utilizing the secure internet banking platform may execute outbound foreign currency wire transfers up to a daily maximum limit of $25,000 USD equivalent. Transfers exceeding this threshold require physical branch verification with valid government-issued photographic identification and source of wealth documentation. Standard cross-border wire processing takes between 1 and 3 international banking days via the SWIFT interbank network.",
                "doc_hi": "इंटरनेट बैंकिंग का उपयोग करने वाले खुदरा ग्राहक $25,000 अमरीकी डालर के बराबर की दैनिक सीमा तक विदेशी मुद्रा वायर ट्रांसफर कर सकते हैं। इस सीमा से अधिक के ट्रांसफर के लिए शाखा में जाकर पहचान और धन के स्रोत के दस्तावेजों का सत्यापन आवश्यक है। स्विफ्ट नेटवर्क के माध्यम से स्थानांतरण में 1 से 3 कार्य दिवस लगते हैं।",
                "doc_te": "ఇంటర్నెట్ బ్యాంకింగ్ ఉపయోగించే ఖాతాదారులు రోజుకు గరిష్టంగా $25,000 అమెరికన్ డాలర్ల వరకు అంతర్జాతీయ వైర్ బదిలీలను చేయవచ్చు. ఈ పరిమితి దాటితే ప్రభుత్వ గుర్తింపు కార్డు మరియు ఆదాయ ఆధారాలతో నేరుగా బ్యాంక్ బ్రాంచ్‌ను సంప్రదించి ధృవీకరించుకోవాలి. SWIFT నెట్‌వర్క్ ద్వారా జరిగే ఈ లావాదేవీలు పూర్తి కావడానికి 1 నుండి 3 అంతర్జాతీయ బ్యాంకింగ్ పని దినాలు పడుతుంది.",
                "doc_teen": "Retail banking customers internet banking dwara foreign currency wire transfers daily maximum limit $25,000 USD varaku execute chesukovachu. Ee threshold daatithe branch ki velli valid photo ID mariyu source of funds documents tho verify cheyali. SWIFT interbank network dwara transfer complete avvadaniki 1 to 3 international banking days paduthundi."
            },
            {
                "topic": "Fixed Deposit Early Withdrawal Penalty",
                "task_en": "What penalty is deducted upon early closure of a fixed term deposit?",
                "task_hi": "सावधि जमा (FD) को समय से पहले बंद करने पर कितना जुर्माना काटा जाता है?",
                "task_te": "ఫిక్స్‌డ్ డిపాజిట్‌ను గడువుకు ముందే రద్దు చేసుకుంటే ఎంత పెనాల్టీ విధిస్తారు?",
                "task_teen": "Fixed deposit premature withdrawal chesthe penalty entha deduct avtundi?",
                "doc_en": "Premature liquidation of a fixed term deposit prior to the contracted maturity date incurs a penalty of 1.00% deducted from the interest rate applicable for the actual tenure the deposit remained invested with the bank. Deposited principal funds remain 100% safeguarded and are never reduced. In cases where the deposit has completed less than 7 days of total tenure, zero interest is credited and only the principal sum is remitted.",
                "doc_hi": "परिपक्वता तिथि से पहले सावधि जमा को बंद करने पर बैंक द्वारा उस अवधि के लिए लागू ब्याज दर में से 1.00% का जुर्माना काटा जाता है। मूलधन पूरी तरह से सुरक्षित रहता है और कभी कम नहीं होता। यदि जमा 7 दिनों से कम समय तक रहा है, तो कोई ब्याज नहीं दिया जाता है और केवल मूल राशि वापस की जाती है।",
                "doc_te": "కాలపరిమితి ముగియక ముందే ఫిక్స్‌డ్ టర్మ్ డిపాజిట్‌ను రద్దు చేసుకుంటే, డిపాజిట్ కొనసాగిన కాలానికి వర్తించే వడ్డీ రేటు నుండి 1.00% పెనాల్టీని తగ్గిస్తారు. కస్టమర్ అసలు మొత్తం (ప్రిన్సిపల్) పూర్తిగా సురక్షితంగా ఉంటుంది. ఒకవేళ డిపాజిట్ ప్రారంభించిన 7 రోజులలోపే రద్దు చేసుకుంటే ఎలాంటి వడ్డీ చెల్లించబడదు, కేవలం అసలు మొత్తం మాత్రమే తిరిగి ఇవ్వబడుతుంది.",
                "doc_teen": "Maturity date ki munde fixed deposit liquidate chesthe, actual tenure ki applicable ayye interest rate nunchi 1.00% penalty deduct chestharu. Deposited principal amount safe ga untundi, daantlo cuts undavu. Deposit start chesina 7 days lopala close chesthe no interest credit avtundi, kevalam principal amount matrame remit chestharu."
            },
            {
                "topic": "Credit Card Dispute Timeframe",
                "task_en": "Within how many days must an unauthorized credit card charge be disputed?",
                "task_hi": "अनधिकृत क्रेडिट कार्ड शुल्क पर कितने दिनों के भीतर विवाद दर्ज किया जाना चाहिए?",
                "task_te": "క్రెడిట్ కార్డులో జరిగిన అనధికారిక లావాదేవీలపై ఎన్ని రోజుల్లోగా ఫిర్యాదు చేయాలి?",
                "task_teen": "Unauthorized credit card transactions ni enni days lo dispute cheyali?",
                "doc_en": "Cardholders who identify unauthorized or fraudulent transactions on their billing statement must file a formal chargeback dispute within 60 calendar days from the statement generation date. Upon receiving the dispute form and cardholder declaration, the bank issues a temporary provisional credit within 5 business days while initiating merchant arbitration via Visa or Mastercard dispute settlement channels.",
                "doc_hi": "अपने विवरण में अनधिकृत या धोखाधड़ी वाले लेनदेन की पहचान करने वाले कार्डधारकों को विवरण जारी होने की तारीख से 60 दिनों के भीतर औपचारिक विवाद दर्ज करना होगा। विवाद प्राप्त होने पर, बैंक वीजा या मास्टरकार्ड के माध्यम से जांच करते हुए 5 दिनों के भीतर अस्थायी क्रेडिट जारी करता है।",
                "doc_te": "క్రెడిట్ కార్డు బిల్లింగ్ స్టేట్‌మెంట్‌లో అనధికారిక లేదా మోసపూరిత లావాదేవీలను గుర్తించిన కార్డుదారులు స్టేట్‌మెంట్ జారీ చేసిన తేదీ నుండి 60 రోజుల్లోగా అధికారిక వివాదాన్ని (డిస్ప్యూట్) నమోదు చేయాలి. దరఖాస్తు అందిన 5 పని దినాల్లోగా బ్యాంక్ తాత్కాలిక క్రెడిట్‌ను ఖాతాలో జమ చేస్తుంది మరియు వీసా లేదా మాస్టర్‌కార్డ్ నెట్‌వర్క్ ద్వారా విచారణను ప్రారంభిస్తుంది.",
                "doc_teen": "Card billing statement lo unauthorized transactions chuste statement date nunchi 60 calendar days lopala formal chargeback dispute file cheyali. Dispute form receive chesukunna 5 business days lo bank provisional credit issue chesthundi mariyu Visa/Mastercard channels dwara merchant arbitration initiate chesthundi."
            },
            {
                "topic": "Savings Account KYC Update Schedule",
                "task_en": "How frequently must banking customers update their Know Your Customer (KYC) records?",
                "task_hi": "बैंकिंग ग्राहकों को कितनी बार अपने केवाईसी (KYC) रिकॉर्ड को अपडेट करना होगा?",
                "task_te": "ఖాతాదారులు తమ KYC వివరాలను ఎంత కాలానికి ఒకసారి అప్‌డేట్ చేయాలి?",
                "task_teen": "Banking customers KYC records ni entha frequency tho refresh cheyali?",
                "doc_en": "In compliance with central banking anti-money laundering mandates, commercial banks categorize accounts by risk profiles for periodic KYC updates. High-risk designated customers must submit fresh identity verification and proof of residential address every 2 years. Medium-risk account holders refresh records every 8 years, whereas low-risk retail customers undergo periodic review every 10 years. Non-compliant accounts face debit freezing after 90 days notification.",
                "doc_hi": "एंटी-मनी लॉन्ड्रिंग नियमों के अनुसार, बैंक समय-समय पर केवाईसी अपडेट के लिए खातों को जोखिम के आधार पर वर्गीकृत करते हैं। उच्च जोखिम वाले ग्राहकों को हर 2 साल में नए पहचान और पते के प्रमाण जमा करने होंगे। मध्यम जोखिम वाले ग्राहक हर 8 साल में और कम जोखिम वाले ग्राहक हर 10 साल में रिकॉर्ड अपडेट करते हैं। अनुपालन न करने पर खाता फ्रीज हो सकता है।",
                "doc_te": "మనీ లాండరింగ్ నిరోధక నిబంధనల ప్రకారం, బ్యాంకులు రిస్క్ ప్రొఫైల్స్ ఆధారంగా కస్టమర్ల KYC ని అప్‌డేట్ చేస్తాయి. అధిక రిస్క్ (హై-రిస్క్) కేటగిరీ కస్టమర్లు ప్రతి 2 సంవత్సరాలకు ఒకసారి తాజా గుర్తింపు మరియు చిరునామా పత్రాలను సమర్పించాలి. మీడియం రిస్క్ ఖాతాదారులు ప్రతి 8 సంవత్సరాలకు, సాధారణ లో-రిస్క్ కస్టమర్లు ప్రతి 10 సంవత్సరాలకు ఒకసారి KYC పూర్తి చేయాలి. స్పందించకపోతే 90 రోజుల తర్వాత డెబిట్ లావాదేవీలు నిలిపివేస్తారు.",
                "doc_teen": "Anti-money laundering mandates prakaram banks risk profiles batti periodic KYC update chesthayi. High-risk customers prathi 2 years ki fresh ID mariyu address proof submit cheyali. Medium-risk holders 8 years ki, low-risk retail customers 10 years ki records refresh cheyali. Compliance follow avvakapothe 90 days notice tharuvatha debit transactions freeze avtayi."
            },
            {
                "topic": "ATM Cash Withdrawal Limits",
                "task_en": "What is the daily domestic ATM cash withdrawal limit and free monthly transaction count?",
                "task_hi": "दैनिक घरेलू एटीएम नकद निकासी सीमा और मुफ्त मासिक लेनदेन की संख्या क्या है?",
                "task_te": "రోజువారీ ATM నగదు ఉపసంహరణ పరిమితి మరియు నెలకు ఉచిత లావాదేవీల సంఖ్య ఎంత?",
                "task_teen": "Daily ATM cash withdrawal limit mariyu free monthly transactions count entha?",
                "doc_en": "Standard retail debit cardholders are permitted a daily domestic ATM cash withdrawal ceiling of $1,000 or local currency equivalent across all affiliated banking networks. Customers are entitled to 5 complimentary cash withdrawals per calendar month at own-bank automated tellers and 3 complimentary withdrawals at non-affiliated domestic terminals. Additional transactions beyond the threshold incur an automated convenience fee of $2.50 per withdrawal.",
                "doc_hi": "मानक डेबिट कार्डधारकों को सभी एटीएम नेटवर्क पर $1,000 की दैनिक घरेलू नकद निकासी सीमा की अनुमति है। ग्राहक अपने बैंक के एटीएम पर प्रति माह 5 मुफ्त निकासी और अन्य बैंकों के एटीएम पर 3 मुफ्त निकासी के हकदार हैं। सीमा से अधिक अतिरिक्त निकासी पर प्रति लेनदेन $2.50 का शुल्क लगता है।",
                "doc_te": "సాధారణ డెబిట్ కార్డుదారులకు రోజువారీ దేశీయ ATM నగదు విత్‌డ్రాయల్ పరిమితి గరిష్టంగా $1,000 గా నిర్ణయించబడింది. కస్టమర్లకు తమ సొంత బ్యాంక్ ATMలలో నెలకు 5 ఉచిత ఉపసంహరణలు మరియు ఇతర బ్యాంకుల ATMలలో 3 ఉచిత లావాదేవీలు లభిస్తాయి. పరిమితి దాటిన తర్వాత చేసే ప్రతి అదనపు లావాదేవీకి $2.50 కన్వీనియన్స్ ఫీజు విధించబడుతుంది.",
                "doc_teen": "Standard debit cardholders ki daily domestic ATM cash withdrawal limit $1,000 USD equivalent untundi. Calendar month lo own-bank ATMs lo 5 free withdrawals mariyu other bank terminals lo 3 free withdrawals claim chesukovachu. Ee threshold daatithe prathi extra withdrawal ki $2.50 convenience fee automatically deduct avtundi."
            },
            {
                "topic": "Personal Loan Foreclosure Charges",
                "task_en": "What are the foreclosure charges for early settlement of floating rate personal loans?",
                "task_hi": "फ्लोटिंग दर व्यक्तिगत ऋण के समयपूर्व निपटान के लिए क्या शुल्क हैं?",
                "task_te": "ఫ్లోటింగ్ రేట్ వ్యక్తిగత రుణాన్ని గడువుకు ముందే చెల్లించి రద్దు చేస్తే ఛార్జీలు ఏమిటి?",
                "task_teen": "Floating rate personal loan prepayment kani foreclosure charges entha untayi?",
                "doc_en": "Under prevailing banking ombudsman directives, commercial lenders cannot levy prepayment penalties or foreclosure charges on floating-rate retail personal loans or home advances settled ahead of tenure. Borrowers may remit partial prepayments or fully close the outstanding balance via digital net banking without penalty. However, fixed-rate term loans closed within the first 12 months attract a standard 2.00% prepayment penalty on the outstanding principal.",
                "doc_hi": "बैंकिंग लोकपाल के निर्देशों के अनुसार, बैंक फ्लोटिंग-दर वाले व्यक्तिगत या गृह ऋणों पर समय से पहले बंद करने का कोई शुल्क नहीं लगा सकते हैं। उधारकर्ता बिना किसी जुर्माने के डिजिटल नेट बैंकिंग के माध्यम से शेष राशि को बंद कर सकते हैं। हालांकि, पहले 12 महीनों के भीतर बंद किए गए फिक्स्ड-रेट ऋणों पर 2.00% का पूर्वभुगतान जुर्माना लगता है।",
                "doc_te": "బ్యాంకింగ్ అంబుడ్స్‌మన్ మార్గదర్శకాల ప్రకారం, ఫ్లోటింగ్ వడ్డీ రేటు కలిగిన వ్యక్తిగత లేదా గృహ రుణాలను గడువుకు ముందే చెల్లించినట్లయితే ఎలాంటి ముందస్తు రద్దు (ఫోర్‌క్లోజర్) ఛార్జీలు విధించకూడదు. కస్టమర్లు ఎలాంటి పెనాల్టీ లేకుండా నెట్ బ్యాంకింగ్ ద్వారా లోన్ మొత్తాన్ని క్లోజ్ చేయవచ్చు. అయితే, ఫిక్స్‌డ్-రేట్ లోన్లను మొదటి 12 నెలల్లో క్లోజ్ చేస్తే మిగిలిన అసలుపై 2.00% పెనాల్టీ విధిస్తారు.",
                "doc_teen": "Banking ombudsman guidelines prakaram floating-rate personal loans kani home loans kani early ga settle chesthe zero prepayment penalties kani foreclosure charges untayi. Net banking dwara outstanding balance clear chesukovachu. Kani fixed-rate loans ni first 12 months lo close chesthe outstanding principal pai 2.00% prepayment penalty apply avtundi."
            },
            {
                "topic": "Home Loan Loan-to-Value Ratio",
                "task_en": "What is the maximum Loan-to-Value (LTV) ratio allowed for residential property loans?",
                "task_hi": "आवासीय संपत्ति ऋण के लिए अनुमत अधिकतम ऋण-से-मूल्य (LTV) अनुपात क्या है?",
                "task_te": "గృహ రుణాల మంజూరులో అనుమతించబడే గరిష్ట లోన్-టు-వాల్యూ (LTV) నిష్పత్తి ఎంత?",
                "task_teen": "Residential home loans lo maximum Loan-to-Value (LTV) ratio entha allow chestharu?",
                "doc_en": "Mortgage underwriting guidelines stipulate maximum Loan-to-Value (LTV) thresholds to manage credit risk exposure. For residential property acquisitions valued up to $100,000, banks may finance up to an 85% LTV ratio. For properties valued between $100,000 and $300,000, the statutory cap is set at 80% LTV. High-value luxury residences exceeding $300,000 are subject to a maximum 75% LTV financing limit, requiring borrowers to contribute the remaining equity as down payment.",
                "doc_hi": "बंधक दिशानिर्देश क्रेडिट जोखिम के प्रबंधन के लिए अधिकतम ऋण-से-मूल्य (एलटीवी) सीमा निर्धारित करते हैं। $100,000 तक की आवासीय संपत्तियों के लिए बैंक 85% तक वित्तपोषण कर सकते हैं। $100,000 और $300,000 के बीच की संपत्तियों के लिए सीमा 80% है। $300,000 से अधिक की लक्जरी संपत्तियों पर अधिकतम 75% एलटीवी लागू होता है।",
                "doc_te": "క్రెడిట్ రిస్క్ నిర్వహణ కొరకు హోమ్ లోన్ మార్గదర్శకాల్లో గరిష్ట లోన్-టు-వాల్యూ (LTV) పరిమితులను నిర్ణయించారు. $100,000 వరకు విలువ చేసే నివాస గృహాలకు బ్యాంకులు 85% వరకు లోన్ ఇస్తాయి. $100,000 నుండి $300,000 మధ్య విలువ గల ఆస్తులకు గరిష్ట పరిమితి 80% LTV. $300,000 కంటే ఎక్కువ విలువైన లగ్జరీ ఇళ్లకు గరిష్టంగా 75% మాత్రమే లోన్ మంజూరు చేస్తారు, మిగిలిన మొత్తాన్ని కొనుగోలుదారు డౌన్ పేమెంట్‌గా చెల్లించాలి.",
                "doc_teen": "Home mortgage underwriting lo credit risk manage cheyadaniki Loan-to-Value (LTV) caps untayi. $100,000 varaku unde properties ki banks up to 85% LTV finance chesthayi. $100,000 nunchi $300,000 madhyalo unte 80% LTV statutory cap untundi. $300,000 kante ekkuva unna luxury properties ki maximum 75% LTV limit untundi, migatha amount buyer down payment ga pettali."
            },
            {
                "topic": "Savings Minimum Balance Shortfall Penalty",
                "task_en": "What is the penalty for failing to maintain the monthly average balance in a savings account?",
                "task_hi": "बचत खाते में मासिक औसत शेष राशि बनाए रखने में विफल रहने पर क्या जुर्माना है?",
                "task_te": "పొదుపు ఖాతాలో కనీస నెలవారీ సగటు నిల్వను నిర్వహించకపోతే ఎంత జరిమానా విధిస్తారు?",
                "task_teen": "Savings account lo monthly average balance maintain cheyakapothe penalty entha?",
                "doc_en": "Tier-1 premium savings accounts require the accountholder to maintain a Monthly Average Balance (MAB) of $500 across calendar months. If the closing balance falls below this benchmark, an automated tiered shortfall fee is assessed: shortfalls between 1% and 50% incur a $10 monthly maintenance fee, while shortfalls exceeding 50% incur a $15 fee. Accounts held by students, senior citizens, and payroll employees are fully exempt from minimum balance requirements.",
                "doc_hi": "प्रीमियम बचत खातों में $500 का मासिक औसत शेष (MAB) बनाए रखना आवश्यक है। यदि शेष राशि इससे कम होती है, तो 1% से 50% की कमी पर $10 और 50% से अधिक की कमी पर $15 का शुल्क लिया जाता है। छात्रों, वरिष्ठ नागरिकों और वेतन खाताधारकों को न्यूनतम शेष राशि की आवश्यकता से पूरी छूट दी गई है।",
                "doc_te": "ప్రీమియం పొదుపు ఖాతాదారులు తమ ఖాతాలో నెలకు కనీసం $500 సగటు నిల్వ (MAB) ఉండేలా చూసుకోవాలి. నిల్వ తక్కువైతే లోటు శాతాన్ని బట్టి జరిమానా విధిస్తారు: 1% నుండి 50% వరకు లోటు ఉంటే నెలకు $10, 50% కంటే ఎక్కువ లోటు ఉంటే $15 రుసుము వసూలు చేస్తారు. విద్యార్థులు, సీనియర్ సిటిజన్లు మరియు శాలరీ అకౌంట్ కలిగిన వారికి కనీస నిల్వ నిబంధనల నుండి పూర్తి మినహాయింపు ఉంది.",
                "doc_teen": "Premium savings accounts lo $500 Monthly Average Balance (MAB) maintain cheyali. Benchmark kante taggithe tiered penalty paduthundi: 1% to 50% shortfall unte $10 fee, 50% kante ekkuva shortfall unte $15 maintenance charge paduthundi. Students, senior citizens mariyu salary account holders ki minimum balance rules nunchi complete exemption untundi."
            },
            {
                "topic": "Foreign Currency Transaction Markup",
                "task_en": "What percentage markup fee applies to overseas debit card point-of-sale transactions?",
                "task_hi": "विदेशी डेबिट कार्ड प्वाइंट-ऑफ-सेल लेनदेन पर कितने प्रतिशत मार्कअप शुल्क लागू होता है?",
                "task_te": "విదేశాలలో డెబిట్ కార్డు ద్వారా చేసే లావాదేవీలపై ఎంత శాతం మార్కప్ రుసుము విధిస్తారు?",
                "task_teen": "Overseas point-of-sale card transactions pai foreign currency markup percentage entha?",
                "doc_en": "When debit or credit cards are utilized for transactions denominated in currencies other than the account's domestic currency, a standard Foreign Currency Transaction Markup Fee of 2.50% is added to the interbank exchange rate determined by Visa or Mastercard on the settlement date. In addition, overseas ATM cash withdrawals attract a flat international terminal access fee of $4.00 plus the standard 2.50% currency conversion fee.",
                "doc_hi": "जब विदेशी मुद्रा में लेनदेन के लिए कार्ड का उपयोग किया जाता है, तो वीज़ा या मास्टरकार्ड की विनिमय दर पर 2.50% का मानक विदेशी मुद्रा मार्कअप शुल्क जोड़ा जाता है। इसके अलावा, विदेशी एटीएम से नकद निकासी पर $4.00 का फ्लैट शुल्क और 2.50% मुद्रा रूपांतरण शुल्क लगता है।",
                "doc_te": "విదేశీ కరెన్సీలలో డెబిట్ లేదా క్రెడిట్ కార్డులను స్వైప్ చేసినప్పుడు, సెటిల్‌మెంట్ రోజున వీసా లేదా మాస్టర్‌కార్డ్ నిర్ణయించిన మారకం రేటుపై అదనంగా 2.50% ఫారిన్ కరెన్సీ మార్కప్ ఫీజు జోడించబడుతుంది. దీనికి అదనంగా, విదేశీ ATMలలో నగదు విత్‌డ్రా చేస్తే ఫ్లాట్ అంతర్జాతీయ టెర్మినల్ ఛార్జ్ $4.00 మరియు 2.50% కరెన్సీ మార్పిడి రుసుము విధిస్తారు.",
                "doc_teen": "Domestic currency kakunda foreign currencies lo card use chesetappudu Visa/Mastercard exchange rate pai 2.50% Foreign Currency Markup Fee add avtundi. Daanitho paatu overseas ATM cash withdrawals ki flat $4.00 international access fee plus 2.50% currency conversion fee charge chestharu."
            },
            {
                "topic": "Tax Deduction at Source on Interest",
                "task_en": "What is the threshold and rate for Tax Deducted at Source on deposit interest?",
                "task_hi": "जमा ब्याज पर स्रोत पर कर कटौती (TDS) की सीमा और दर क्या है?",
                "task_te": "డిపాజిట్లపై వచ్చే వడ్డీకి వర్తించే మూలం వద్ద పన్ను తగ్గింపు (TDS) పరిమితి మరియు రేటు ఎంత?",
                "task_teen": "Deposit interest pai Tax Deducted at Source (TDS) threshold mariyu rate entha?",
                "doc_en": "Under statutory tax compliance regulations, financial institutions are obligated to deduct Tax Deducted at Source (TDS) at the rate of 10% on interest earned across fixed and recurring deposits if total annual interest income exceeds $400 ($600 for registered senior citizens). If the customer fails to furnish a valid Permanent Tax Identification Number, TDS is deducted at the punitive rate of 20%. Eligible taxpayers may submit Form 15G or 15H at the fiscal year start to claim zero deduction.",
                "doc_hi": "कर नियमों के तहत, यदि कुल वार्षिक ब्याज आय $400 (वरिष्ठ नागरिकों के लिए $600) से अधिक है, तो बैंक 10% की दर से टीडीएस काटते हैं। यदि वैध पैन कार्ड प्रदान नहीं किया जाता है, तो 20% की दंडात्मक दर से टीडीएस काटा जाता है। पात्र करदाता छूट का दावा करने के लिए वित्तीय वर्ष की शुरुआत में फॉर्म 15G या 15H जमा कर सकते हैं।",
                "doc_te": "ఆదాయపు పన్ను చట్ట నిబంధనల ప్రకారం, ఫిక్స్‌డ్ మరియు రికరింగ్ డిపాజిట్లపై వార్షిక వడ్డీ ఆదాయం $400 (సీనియర్ సిటిజన్లకు $600) దాటితే బ్యాంకులు 10% చొప్పున TDS పన్నును మినహాయిస్తాయి. ఖాతాదారుడు సరైన టాక్స్ ఐడెంటిఫికేషన్ నంబర్ (పాన్ కార్డు) సమర్పించకపోతే 20% భారీ రేటుతో TDS కట్ చేస్తారు. పన్ను పరిధిలోకి రాని వారు ఆర్థిక సంవత్సరం ప్రారంభంలో ఫారం 15G లేదా 15H సమర్పించి మినహాయింపు పొందవచ్చు.",
                "doc_teen": "Tax regulations prakaram fixed/recurring deposits pai annual interest $400 ($600 for senior citizens) daatithe bank 10% TDS deduct chesthundi. Valid Tax ID (PAN) submit cheyakapothe 20% punitive rate tho TDS cut avtundi. Tax liability leni eligible individuals fiscal year start lo Form 15G kani 15H kani submit chesi zero deduction claim chesukovachu."
            }
        ]
    }
]
