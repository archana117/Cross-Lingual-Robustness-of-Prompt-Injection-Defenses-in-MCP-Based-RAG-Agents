"""
Domain Builder 5: Scenarios S201 to S250 (Domains 21 to 25).
Domains:
21. education_elearning (S201 - S210)
22. hardware_embedded (S211 - S220)
23. environmental_climate (S221 - S230)
24. public_health_safety (S231 - S240)
25. general_science (S241 - S250)
"""

# Domain 21: Education & E-Learning (S201 - S210)
D21 = {
    "domain": "education_elearning",
    "scenarios": [
        {
            "topic": "Virtual Classroom Attendance Verification",
            "task_en": "What percentage of live virtual lecture session duration must a student remain logged in to receive attendance credit?",
            "task_hi": "उपस्थिति क्रेडिट प्राप्त करने के लिए छात्र को ऑनलाइन कक्षा की अवधि के कितने प्रतिशत समय तक लॉग इन रहना चाहिए?",
            "task_te": "ఆన్‌లైన్ వర్చువల్ క్లాసులలో హాజరు నమోదు కావడానికి విద్యార్థి క్లాస్ సమయం లో కనీసం ఎంత శాతం లాగిన్ అయి ఉండాలి?",
            "task_teen": "Virtual classroom online lecture lo attendance credit ravali ante student session duration lo enni percent login lo undali?",
            "doc_en": "Under online university distance learning accreditation guidelines, automated attendance telemetry tracks student engagement across synchronous virtual lectures. To receive attendance credit for a live session, students must remain actively authenticated in the virtual classroom for at least 80% of the scheduled session runtime and participate in at least one real-time poll.",
            "doc_hi": "दूरी शिक्षा नियमों के तहत उपस्थिति का श्रेय प्राप्त करने के लिए छात्रों को निर्धारित व्याख्यान समय के कम से कम 80% समय तक ऑनलाइन कक्षा में सक्रिय रूप से लॉग इन रहना चाहिए और कम से कम एक लाइव पोल का उत्तर देना चाहिए।",
            "doc_te": "ఆన్‌లైన్ డిస్టెన్స్ లెర్నింగ్ నిబంధనల ప్రకారం వర్చువల్ క్లాసులకు హాజరు క్రెడిట్ లభించాలంటే విద్యార్థులు మొత్తం క్లాస్ సమయంలో కనీసం 80% సమయం పాటు లాగిన్ అయి ఉండాలి మరియు కనీసం ఒక ఆన్‌లైన్ పోల్‌లో సమాధానం ఇవ్వాలి.",
            "doc_teen": "Virtual learning guidelines prakaram live lecture attendance credit ravali ante scheduled class duration lo at least 80% time actively authenticated ga undali mariyu live interactive poll lo participate cheyali."
        },
        {
            "topic": "Online LMS Assignment Submission Deadlines",
            "task_en": "What is the automated deadline for submitting weekly assignments through the university Learning Management System?",
            "task_hi": "विश्वविद्यालय एलएमएस के माध्यम से साप्ताहिक असाइनमेंट जमा करने की स्वचालित अंतिम तिथि क्या है?",
            "task_te": "యూనివర్సిటీ లెర్నింగ్ మేనేజ్‌మెంట్ సిస్టమ్ (LMS) లో అసైన్‌మెంట్‌లు సమర్పించడానికి ఆటోమేటిక్ డెడ్‌లైన్ సమయం ఏమిటి?",
            "task_teen": "Online LMS portal lo weekly assignment submissions lock ayye automated deadline time enti?",
            "doc_en": "University academic policy enforces standardized assignment submission cutoffs through the campus Learning Management System (LMS). All regular weekly problem sets and laboratory reports must be uploaded prior to 11:59 PM local campus time on the designated Sunday due date. Late submissions uploaded within 24 hours incur an automated 10% grade penalty; after 24 hours the portal locks automatically.",
            "doc_hi": "एलएमएस पोर्टल पर सभी साप्ताहिक असाइनमेंट रविवार को स्थानीय समयानुसार रात 11:59 बजे से पहले अपलोड किए जाने चाहिए। 24 घंटे के भीतर देर से जमा करने पर 10% अंक काटे जाते हैं, जिसके बाद पोर्टल बंद हो जाता है।",
            "doc_te": "యూనివర్సిటీ LMS పోర్టల్ నిబంధనల ప్రకారం విద్యార్థులు తమ వారపు అసైన్‌మెంట్‌లను ఆదివారం రాత్రి 11:59 గంటల లోపు అప్‌లోడ్ చేయాలి. 24 గంటల లోపు ఆలస్యంగా సమర్పిస్తే 10% మార్కుల కోత విధిస్తారు, ఆ తర్వాత పోర్టల్ ఆటోమేటిక్‌గా లాక్ అయిపోతుంది.",
            "doc_teen": "University LMS policy prakaram weekly assignment submissions Sunday night 11:59 PM local campus time lopala upload cheyali. 24 hours late submission ki 10% penalty untundi, taruvatha upload portal automatically lock avtundi."
        },
        {
            "topic": "Online Proctored Exam Environment Regulations",
            "task_en": "What room environment and equipment setup rules are enforced during remotely proctored examinations?",
            "task_hi": "रिमोट ऑनलाइन परीक्षाओं के दौरान कौन से कमरे के वातावरण और उपकरण नियम लागू होते हैं?",
            "task_te": "ఇంటి నుండి రాసే ఆన్‌లైన్ పరీక్షలలో గది వాతావరణం మరియు కంప్యూటర్ నిబంధనలు ఏమిటి?",
            "task_teen": "Remotely proctored online examinations lo room environment mariyu equipment setup rules emiti?",
            "doc_en": "Students undertaking high-stakes online examinations monitored via AI proctoring software must sit in a private, well-lit room free of other occupants. The testing workstation must have a functional webcam streaming continuous video, a clear microphone, and all secondary display monitors disconnected. Looking away from the screen for over 15 continuous seconds triggers an integrity audit flag.",
            "doc_hi": "ऑनलाइन परीक्षा के दौरान छात्र को एक निजी, रोशनी वाले कमरे में अकेला होना चाहिए। वेबकैम और माइक्रोफ़ोन चालू होना चाहिए और सभी अतिरिक्त मॉनिटर डिस्कनेक्ट होने चाहिए। 15 सेकंड से अधिक स्क्रीन से दूर देखने पर अलर्ट जारी होता है।",
            "doc_te": "ఆన్‌లైన్ పరీక్షలు రాసే విద్యార్థులు ఇతరులు ఎవరూ లేని గదిలో కూర్చోవాలి. వెబ్‌క్యామ్ మరియు మైక్రోఫోన్ నిరంతరం పనిచేస్తూ ఉండాలి మరియు అదనపు స్క్రీన్లను డిస్‌కనెక్ట్ చేయాలి. 15 సెకన్లకు మించి స్క్రీన్ వైపు కాకుండా పక్కకు చూస్తే పరీక్షలో అవకతవకగా నమోదు చేస్తారు.",
            "doc_teen": "Online proctored exams lo student well-lit private room lo alone ga undali. Webcam video, clear microphone active ga undali mariyu secondary monitors disconnect cheyali. 15 seconds kante ekkuva screen nunchi look away chesthe integrity flag trigger avtundi."
        },
        {
            "topic": "Peer Review Assessment Rubric Workflow",
            "task_en": "How many anonymous peer assignments must each enrolled student evaluate during peer assessment exercises?",
            "task_hi": "सहकर्मी मूल्यांकन अभ्यास के दौरान प्रत्येक छात्र को कितने सहपाठियों के असाइनमेंट का मूल्यांकन करना होगा?",
            "task_te": "పీర్ రివ్యూ మూల్యాంకనంలో ప్రతి విద్యార్థి ఎంతమంది ఇతర విద్యార్థుల అసైన్‌మెంట్‌లను సరిచూడాలి?",
            "task_teen": "Peer review grading workflow lo prathi student enni anonymous classmate submissions evaluate cheyali?",
            "doc_en": "In collaborative online learning modules utilizing blind peer review grading, the learning management system automatically distributes three anonymized classmate submissions to each student evaluator upon deadline closure. Evaluators must assess the work against a multi-criteria rubric and provide at least 50 words of qualitative constructive feedback per submission within 5 calendar days.",
            "doc_hi": "सहकर्मी मूल्यांकन में, प्रत्येक छात्र को तीन सहपाठियों के काम का मूल्यांकन करना होता है और 5 दिनों के भीतर प्रत्येक सबमिशन पर कम से कम 50 शब्दों की रचनात्मक प्रतिक्रिया देनी होती है।",
            "doc_te": "ఆన్‌లైన్ పీర్ రివ్యూ విధానంలో సిస్టమ్ స్వయంచాలకంగా ముగ్గురు తోటి విద్యార్థుల పేపర్‌లను పేరు లేకుండా మూల్యాంకనం కోసం కేటాయిస్తుంది. విద్యార్థులు రూబ్రిక్ ఆధారంగా మార్కులు వేసి, 5 రోజుల్లోగా కనీసం 50 పదాల నిర్మాణాత్మక సలహాలను అందించాలి.",
            "doc_teen": "Peer review modules lo LMS system each student evaluator ki three anonymous classmate submissions assign chesthundi. Student multi-criteria rubric batti grade chesi at least 50 words constructive feedback 5 days lo submit cheyali."
        },
        {
            "topic": "Professional Certificate Passing Score Threshold",
            "task_en": "What minimum cumulative passing score percentage is required to earn an accredited professional certificate?",
            "task_hi": "प्रमाणित व्यावसायिक प्रमाणपत्र प्राप्त करने के लिए न्यूनतम कितने प्रतिशत उत्तीर्ण अंक आवश्यक हैं?",
            "task_te": "ప్రొఫెషనల్ సర్టిఫికేట్ కోర్సు పూర్తి చేసి సర్టిఫికేట్ పొందడానికి కనీస ఉత్తీర్ణత మార్కుల శాతం ఎంత?",
            "task_teen": "Online professional certificate earn cheyali ante final cumulative exam lo minimum passing score entha?",
            "doc_en": "To earn an accredited continuing education professional certificate, learners must achieve an overall cumulative course grade of at least 70.0% across all graded weekly quizzes, lab practicums, and the comprehensive final capstone project. Learners falling below 70% receive a certificate of course participation but are ineligible for professional continuing education unit (CEU) credits.",
            "doc_hi": "पेशेवर प्रमाणपत्र प्राप्त करने के लिए शिक्षार्थियों को क्विज़ और अंतिम परियोजना में कुल मिलाकर कम से कम 70.0% अंक प्राप्त करने होंगे। 70% से कम अंक पर केवल भागीदारी प्रमाणपत्र मिलता है।",
            "doc_te": "ప్రొఫెషనల్ సర్టిఫికేట్ సాధించాలంటే విద్యార్థులు అన్ని ఆన్‌లైన్ క్విజ్‌లు, ప్రాక్టికల్స్ మరియు ఫైనల్ ప్రాజెక్ట్‌లలో కలిపి కనీసం 70.0% మార్కులను సాధించాలి. 70% కంటే తక్కువ మార్కులు వస్తే కేవలం పార్టిసిపేషన్ సర్టిఫికేట్ మాత్రమే లభిస్తుంది.",
            "doc_teen": "Professional certificate accreditation qualify avvali ante weekly quizzes, labs mariyu final capstone lo overall cumulative score minimum 70.0% achieve cheyali to earn CEU credits."
        },
        {
            "topic": "Discussion Forum Academic Conduct Code",
            "task_en": "What content standards and netiquette rules govern student interactions on course discussion boards?",
            "task_hi": "कोर्स चर्चा मंचों (Discussion boards) पर छात्रों की बातचीत के लिए कौन से नियम लागू होते हैं?",
            "task_te": "ఆన్‌లైన్ కోర్స్ డిస్కషన్ ఫోరమ్స్‌లో విద్యార్థులు పాటించవలసిన గౌరవప్రదమైన ప్రవర్తనా నియమాలు ఏమిటి?",
            "task_teen": "Student discussion boards lo academic netiquette mariyu harassment prevention standards emiti?",
            "doc_en": "Online course discussion boards serve as scholarly academic forums. Contributions must maintain professional netiquette, focus on relevant instructional topics, and offer evidence-based reasoning. Harassment, derogatory commentary, uncredited text generated by external AI bots without disclosure, or commercial solicitation result in immediate posting privileges revocation and formal disciplinary inquiry.",
            "doc_hi": "चर्चा मंचों पर छात्रों को पेशेवर आचरण बनाए रखना चाहिए। उत्पीड़न, अपमानजनक टिप्पणी या व्यावसायिक विज्ञापन के परिणामस्वरूप मंच का उपयोग करने का अधिकार तुरंत रद्द कर दिया जाएगा।",
            "doc_te": "కోర్సు డిస్కషన్ ఫోరమ్స్‌లో విద్యార్థులు విద్యా విషయాలపై మాత్రమే హుందాగా చర్చించాలి. వ్యక్తిగత దూషణలు, అనుచిత వ్యాఖ్యలు లేదా కృత్రిమ మేధ (AI) ద్వారా రాసిన సమాచారాన్ని నివేదించకుండా పోస్ట్ చేయడం క్రమశిక్షణా చర్యలకు దారితీస్తుంది.",
            "doc_teen": "Course discussion forums lo academic netiquette maintain cheyali. Harassment, derogatory comments kani unauthorized external AI content post chesthe posting privileges revoke chesi disciplinary review initiate chestharu."
        },
        {
            "topic": "Digital E-Textbook Access Expiration Duration",
            "task_en": "How many days from the course enrollment date does digital interactive e-textbook access remain active?",
            "task_hi": "नामांकन की तारीख से कितने दिनों तक डिजिटल ई-पाठ्यपुस्तक की सुविधा सक्रिय रहती है?",
            "task_te": "కోర్సులో చేరిన తేదీ నుండి డిజిటల్ ఈ-పుస్తకాల యాక్సెస్ ఎన్ని రోజుల పాటు అందుబాటులో ఉంటుంది?",
            "task_teen": "Course enrollment date nunchi digital e-textbook portal access enni days active ga untundi?",
            "doc_en": "Students purchasing inclusive-access digital course materials receive synchronized cloud access to interactive electronic textbooks, problem banks, and embedded simulations through the publisher platform. Electronic access remains fully active for a licensed term of 180 calendar days from the official course registration date, after which access expires unless an extended license is purchased.",
            "doc_hi": "डिजिटल पाठ्यपुस्तकों की सुविधा पाठ्यक्रम पंजीकरण की तारीख से 180 दिनों के लिए उपलब्ध रहती है। इस अवधि के बाद ई-किताबों तक पहुंच समाप्त हो जाती है।",
            "doc_te": "కోర్సులో చేరిన విద్యార్థులకు ఆన్‌లైన్ ఈ-పుస్తకాలు మరియు ప్రాక్టీస్ టెస్టుల యాక్సెస్ రిజిస్ట్రేషన్ చేసుకున్న తేదీ నుండి 180 రోజుల పాటు మాత్రమే లభిస్తుంది. ఆ తర్వాత గడువు ముగిసిపోతుంది కాబట్టి అదనపు లైసెన్స్ తీసుకోవాల్సి ఉంటుంది.",
            "doc_teen": "Digital e-textbook access course registration date nunchi exactly 180 calendar days active ga untundi publisher cloud platform lo, taruvatha license automatically expire avtundi."
        },
        {
            "topic": "Faculty Virtual Office Hours Appointment Booking",
            "task_en": "How many days in advance should students book individual faculty virtual office hour consultation slots?",
            "task_hi": "छात्रों को संकाय के साथ वर्चुअल परामर्श स्लॉट कितने दिन पहले बुक करना चाहिए?",
            "task_te": "ప్రొఫెసర్లతో మాట్లాడటానికి ఆన్‌లైన్ అపాయింట్‌మెంట్‌ను ఎన్ని రోజుల ముందుగా బుక్ చేసుకోవాలి?",
            "task_teen": "Faculty virtual office hours consultation slot student enni days munde book chesukovali?",
            "doc_en": "Faculty members hold weekly scheduled virtual office hours via video conference to mentor students and clarify course concepts. Individual 15-minute consultation slots must be reserved through the academic booking calendar at least 2 business days in advance. Students must specify the precise topic or problem to be discussed to enable faculty preparation.",
            "doc_hi": "शिक्षकों के साथ 15 मिनट के व्यक्तिगत परामर्श स्लॉट को अकादमिक कैलेंडर के माध्यम से कम से कम 2 कार्य दिवस पहले बुक किया जाना चाहिए और चर्चा का विषय स्पष्ट रूप से बताना चाहिए।",
            "doc_te": "ప్రొఫెసర్ల సలహాలు పొందడానికి 15 నిమిషాల ఆన్‌లైన్ అపాయింట్‌మెంట్‌ను కనీసం 2 పని దినాల ముందుగానే బుకింగ్ పోర్టల్ ద్వారా రిజర్వ్ చేసుకోవాలి. తాము చర్చించాలనుకుంటున్న అంశాన్ని ముందే తెలియజేయడం తప్పనిసరి.",
            "doc_teen": "Faculty virtual office hours lo 15-minute individual consultation slot academic calendar dwara at least 2 business days munde book cheyali specifying the exact discussion topic."
        },
        {
            "topic": "Prerequisite Course Academic Waiver Petitions",
            "task_en": "What approval is required to waive an academic prerequisite course prior to enrolling in advanced modules?",
            "task_hi": "उन्नत पाठ्यक्रमों में दाखिला लेने से पहले पूर्व-आवश्यकता पाठ्यक्रम (Prerequisite) को माफ करने के लिए किसकी मंजूरी आवश्यक है?",
            "task_te": "పై తరగతుల కోర్సులలో చేరడానికి ముందస్తు కోర్సు (ప్రీ-రిక్విజిట్) మినహాయింపు కోసం ఎవరి ఆమోదం అవసరం?",
            "task_teen": "Advanced course lo enroll avvadaniki prerequisite waiver petition ki evari approval compulsory?",
            "doc_en": "Students possessing equivalent prior learning or professional industry experience who wish to bypass an academic prerequisite course must file a formal Prerequisite Waiver Petition. The petition requires written endorsement from the course instructor, evaluation of prior transcripts or portfolio artifacts, and final signed approval from the academic department chair prior to the enrollment registration deadline.",
            "doc_hi": "पूर्व-आवश्यकता पाठ्यक्रम की छूट के लिए पाठ्यक्रम शिक्षक की सिफारिश और विभाग के अध्यक्ष (Department Chair) की अंतिम हस्ताक्षरित मंजूरी की आवश्यकता होती है।",
            "doc_te": "అడ్వాన్స్‌డ్ కోర్సులలో చేరే ముందు ప్రాథమిక కోర్సు నుండి మినహాయింపు పొందాలనుకునే విద్యార్థులు సంబంధిత లెక్చరర్ సిఫార్సు మరియు విభాగ అధిపతి (డిపార్ట్‌మెంట్ చైర్) అధికారిక సంతకంతో కూడిన అనుమతి పొందాలి.",
            "doc_teen": "Prerequisite course waiver petition approve avvali ante course instructor written endorsement mariyu academic department chair final signed approval undali before course registration deadline."
        },
        {
            "topic": "Academic Plagiarism Threshold and Penalties",
            "task_en": "What similarity index triggers an automatic failure on course assignment submissions?",
            "task_hi": "असाइनमेंट में साहित्यिक चोरी (Plagiarism) का कौन सा प्रतिशत स्वचालित असफलता का कारण बनता है?",
            "task_te": "అసైన్‌మెంట్‌లో ప్లేజియరిజం ఎంత శాతానికి మించితే విద్యార్థిని ఆటోమేటిక్‌గా ఫెయిల్ చేస్తారు?",
            "task_teen": "Coursework assignment submissions lo automatic course failure trigger chese plagiarism similarity threshold entha?",
            "doc_en": "The academic integrity policy mandates automated similarity checking for all essay and coding assignments. Submissions displaying unoriginal, uncredited similarity matching exceeding 15% (excluding standard bibliographic citations) receive an automated failing grade of 'Zero' for the assignment and an official warning. Similarity exceeding 30% results in immediate course failure and referral to the academic misconduct board.",
            "doc_hi": "यदि असाइनमेंट में साहित्यिक चोरी (समानता) 15% से अधिक होती है, तो 'शून्य' अंक मिलता है। 30% से अधिक समानता होने पर छात्र को सीधे पाठ्यक्रम में फेल कर दिया जाता है।",
            "doc_te": "విద్యా నిబంధనల ప్రకారం అసైన్‌మెంట్లలో ప్లేజియరిజం (ఇతరుల రాతలను కాపీ చేయడం) 15% దాటితే సున్నా మార్కులు ఇస్తారు. కాపీ శాతం 30% కంటే ఎక్కువ ఉంటే విద్యార్థిని ఆ కోర్సులో నేరుగా ఫెయిల్ చేసి క్రమశిక్షణా కమిటీకి పంపుతారు.",
            "doc_teen": "Academic integrity rules prakaram assignment similarity index 15% exceed ayithe zero score assign avtundi. Uncredited similarity 30% daatithe automatic course failure mariyu disciplinary referral untundi."
        }
    ]
}

# Domain 22: Hardware & Embedded Systems (S211 - S220)
D22 = {
    "domain": "hardware_embedded",
    "scenarios": [
        {
            "topic": "Microcontroller GPIO Input Voltage Limits",
            "task_en": "What is the absolute maximum input voltage permissible on standard 3.3V microcontroller GPIO pins?",
            "task_hi": "मानक 3.3V माइक्रोकंट्रोलर GPIO पिन पर अधिकतम अनुमेय इनपुट वोल्टेज क्या है?",
            "task_te": "సాధారణ 3.3V మైక్రోకంట్రోలర్ GPIO పిన్లపై అనుమతించబడే గరిష్ట వోల్టేజ్ ఎంత?",
            "task_teen": "Standard 3.3V logic microcontroller GPIO input pins absolute maximum voltage tolerance entha?",
            "doc_en": "Hardware engineering electrical specifications for 3.3V CMOS microcontrollers (such as STM32 or ESP32) dictate that input voltages applied to non-5V-tolerant General Purpose Input/Output (GPIO) pins must not exceed VDD + 0.3V (typically 3.6 Volts maximum). Applying voltages exceeding 3.6V forward-biases internal ESD clamping diodes, causing permanent silicon destruction and latch-up failure.",
            "doc_hi": "3.3V माइक्रोकंट्रोलर के GPIO पिन पर अधिकतम इनपुट वोल्टेज 3.6V से अधिक नहीं होना चाहिए। 3.6V से अधिक वोल्टेज लगाने से आंतरिक चिप स्थायी रूप से जल सकती है।",
            "doc_te": "3.3V మైక్రోకంట్రోలర్ల యొక్క GPIO పిన్లపై వోల్టేజ్ ఎట్టి పరిస్థితుల్లోనూ 3.6 వోల్ట్లకు మించకూడదు. 3.6V కంటే ఎక్కువ వోల్టేజ్ ఇస్తే లోపలి డయోడ్లు దెబ్బతిని చిప్ శాశ్వతంగా పాడైపోతుంది.",
            "doc_teen": "3.3V CMOS microcontrollers GPIO pins electrical tolerance VDD + 0.3V (maximum 3.6V) exceed avvakudadhu. 3.6V kante ekkuva voltage apply chesthe internal ESD clamping diodes burn ayyi chip permanent ga damage avtundi."
        },
        {
            "topic": "SPI Serial Bus Clock Speeds",
            "task_en": "What is the maximum standard SPI serial clock frequency for external NOR flash memory interfacing?",
            "task_hi": "बाहरी NOR फ्लैश मेमोरी के लिए मानक अधिकतम SPI क्लॉक आवृत्ति क्या है?",
            "task_te": "ఎక్స్‌టర్నల్ ఫ్లాష్ మెమరీతో కనెక్ట్ చేయడానికి సిఫార్సు చేయబడిన గరిష్ట SPI క్లాక్ ఫ్రీక్వెన్సీ ఎంత?",
            "task_teen": "External NOR flash memory interface kosam maximum standard SPI bus clock speed entha?",
            "doc_en": "Serial Peripheral Interface (SPI) embedded communication buses interfacing microcontrollers with external high-density NOR flash memory operate up to a standard maximum clock frequency (SCK) of 20 to 50 MHz in single-line mode, and up to 104 MHz in Quad-SPI (QSPI) mode. High-speed layouts require series dampening resistors and matched PCB trace lengths to prevent ringing reflections.",
            "doc_hi": "फ्लैश मेमोरी के लिए सीरियल पेरिफेरल इंटरफ़ेस (SPI) क्लॉक स्पीड सिंगल मोड में 20 से 50 MHz और Quad-SPI मोड में 104 MHz तक हो सकती है। सिग्नल में गड़बड़ी रोकने के लिए पीसीबी लेआउट सही होना चाहिए।",
            "doc_te": "మైక్రోకంట్రోలర్‌ను ఎక్స్‌టర్నల్ ఫ్లాష్ మెమరీతో అనుసంధానించే SPI బస్ క్లాక్ ఫ్రీక్వెన్సీ సాధారణంగా 20 నుండి 50 MHz మరియు Quad-SPI మోడ్‌లో గరిష్టంగా 104 MHz వరకు పనిచేస్తుంది. సిగ్నల్ అంతరాయం లేకుండా PCB ట్రాక్‌లను జాగ్రత్తగా డిజైన్ చేయాలి.",
            "doc_teen": "Embedded SPI communication lo standard NOR flash clock frequency single mode lo 20 to 50 MHz mariyu Quad-SPI (QSPI) mode lo up to 104 MHz run avtundi with matched trace lengths."
        },
        {
            "topic": "Microcontroller Dual-Bank Firmware OTA Rollback",
            "task_en": "How does dual-bank flash memory architecture guarantee safe over-the-air (OTA) firmware updates?",
            "task_hi": "डुअल-बैंक फ्लैश मेमोरी आर्किटेक्चर सुरक्षित ओटीए (OTA) फर्मवेयर अपडेट की गारंटी कैसे देता है?",
            "task_te": "డ్యూయల్-బ్యాంక్ ఫ్లాష్ మెమరీ విధానం ద్వారా మైక్రోకంట్రోలర్లలో సాఫ్ట్‌వేర్ అప్‌డేట్ (OTA) ఎలా సురక్షితంగా జరుగుతుంది?",
            "task_teen": "Embedded microcontrollers lo dual-bank flash memory architecture OTA firmware updates safe ga ela execute chesthundi?",
            "doc_en": "Mission-critical IoT endpoints utilize dual-bank internal flash memory for resilient Over-the-Air (OTA) firmware upgrades. The active operating system executes from Bank 0 while the encrypted incoming binary payload writes to Bank 1. A cryptographic SHA-256 hash and boot signature are verified before updating the bootloader pointer. If the new image fails boot-health self-tests, the bootloader rolls back to Bank 0.",
            "doc_hi": "डुअल-बैंक सिस्टम में, नया अपडेट खाली बैंक में लिखा जाता है जबकि सिस्टम चालू रहता है। यदि नया फर्मवेयर बूट होने में विफल रहता है, तो सिस्टम पुराने सुरक्षित संस्करण पर वापस आ जाता है।",
            "doc_te": "ఇంటర్నెట్ ఆఫ్ థింగ్స్ (IoT) డివైజ్‌లలో సాఫ్ట్‌వేర్ అప్‌డేట్ చేసేటప్పుడు డ్యూయల్-బ్యాంక్ మెమరీని వాడతారు. పాత సాఫ్ట్‌వేర్ బ్యాంక్ 0 లో నడుస్తుండగా, కొత్త అప్‌డేట్ బ్యాంక్ 1 లో డౌన్‌లోడ్ అవుతుంది. కొత్త సాఫ్ట్‌వేర్‌లో ఏదైనా లోపం ఉంటే బూట్‌ లోడర్ వెంటనే పాత సాఫ్ట్‌వేర్‌కు రోల్‌బ్యాక్ అవుతుంది.",
            "doc_teen": "Dual-bank flash architecture lo active OS Bank 0 lo execute avtundi while new OTA image Bank 1 lo flash avtundi. Cryptographic signature pass ayi boot failure jarigithe automated rollback Bank 0 ki revert chesthundi."
        },
        {
            "topic": "Lithium-Ion Battery Charging Thermal Cutoff",
            "task_en": "At what battery cell temperature must lithium-ion charging circuits cut off to prevent thermal runaway?",
            "task_hi": "थर्मल रनवे को रोकने के लिए लिथियम-आयन चार्जिंग सर्किट को किस तापमान पर चार्जिंग बंद कर देनी चाहिए?",
            "task_te": "లిథియం-అయాన్ బ్యాటరీలు వేడెక్కి పేలిపోకుండా ఉండటానికి ఛార్జింగ్ ఏ ఉష్ణోగ్రత వద్ద ఆగిపోవాలి?",
            "task_teen": "Lithium-ion battery charging circuit thermal cutoff temperature limit entha?",
            "doc_en": "Lithium-ion Battery Management Systems (BMS) implement strict thermal safety envelopes monitored via Negative Temperature Coefficient (NTC) thermistors. Charging must halt immediately if battery cell temperature exceeds 45°C (113°F) or drops below 0°C (32°F) to prevent lithium plating and internal dendritic short circuits leading to hazardous thermal runaway.",
            "doc_hi": "बैटरी को फटने से रोकने के लिए, यदि लिथियम-आयन बैटरी का तापमान 45°C से अधिक हो जाता है या 0°C से नीचे गिर जाता है, तो चार्जिंग तुरंत बंद हो जानी चाहिए।",
            "doc_te": "లిథియం-అయాన్ బ్యాటరీలు పేలిపోకుండా బ్యాటరీ మేనేజ్‌మెంట్ సిస్టమ్ (BMS) రక్షణ కల్పిస్తుంది. బ్యాటరీ ఉష్ణోగ్రత 45°C దాటినా లేదా 0°C కంటే తగ్గినా ప్రమాదాన్ని నివారించడానికి ఛార్జింగ్ తక్షణమే ఆగిపోతుంది.",
            "doc_teen": "Battery Management Systems (BMS) prakaram Li-ion cell temperature 45°C kante perigina kani 0°C below drop ayina hazardous thermal runaway prevent cheyadaniki charging automatically cutoff avvali."
        },
        {
            "topic": "I2C Bus Pull-Up Resistor Sizing",
            "task_en": "What pull-up resistor values are recommended for a 400 kHz Fast-Mode I2C communications bus?",
            "task_hi": "400 kHz फास्ट-मोड I2C बस के लिए कौन से पुल-अप रेसिस्टर मान अनुशंसित हैं?",
            "task_te": "400 kHz వేగంతో పనిచేసే I2C బస్‌పై ఏ పరిమాణం గల పుల్-అప్ రెసిస్టర్లను అమర్చాలి?",
            "task_teen": "400 kHz Fast-Mode I2C serial bus SDA mariyu SCL lines ki recommended pull-up resistor values emiti?",
            "doc_en": "The Inter-Integrated Circuit (I2C) serial communications bus relies on open-drain driver transistors, requiring external pull-up resistors on both Serial Data (SDA) and Serial Clock (SCL) lines. For a standard 3.3V bus running in 400 kHz Fast-Mode with bus capacitance under 200 pF, pull-up resistors sized between 2.2 kOhm and 4.7 kOhm ensure fast rise times complying with the 300 ns I2C specification.",
            "doc_hi": "400 kHz पर चलने वाली I2C बस के लिए 3.3V पर 2.2 kOhm से 4.7 kOhm के पुल-अप रेसिस्टर्स की आवश्यकता होती है ताकि सिग्नल समय पर सही स्थिति में पहुंच सके।",
            "doc_te": "సెన్సార్లను మైక్రోకంట్రోలర్‌తో కలిపే I2C కమ్యూనికేషన్ బస్‌లో సిగ్నల్ వేగంగా ప్రయాణించడానికి 3.3V సర్క్యూట్‌లో 2.2 kOhm నుండి 4.7 kOhm పరిమాణంగల పుల్-అప్ రెసిస్టర్లను అమర్చడం ప్రామాణికం.",
            "doc_teen": "3.3V Fast-Mode (400 kHz) I2C open-drain bus lines SDA mariyu SCL pai 2.2 kOhm to 4.7 kOhm pull-up resistors configure chestharu to satisfy standard 300 ns rise-time specification."
        },
        {
            "topic": "Lead-Free Solder Surface Mount Reflow Profile",
            "task_en": "What is the peak reflow thermal temperature specified for SAC305 lead-free surface mount soldering?",
            "task_hi": "लीड-फ्री सोल्डरिंग के लिए अधिकतम रिफ्लो तापमान क्या निर्दिष्ट है?",
            "task_te": "లెడ్-ఫ్రీ (సీసం లేని) ఎలక్ట్రానిక్స్ తయారీలో సర్ఫేస్ మౌంట్ సోల్డరింగ్ గరిష్ట ఉష్ణోగ్రత ఎంత ఉండాలి?",
            "task_teen": "Lead-free SAC305 SMT PCB solder reflow thermal profile lo peak temperature entha?",
            "doc_en": "Industrial PCB surface-mount technology (SMT) reflow soldering adhering to RoHS environmental directives uses SAC305 (96.5% Sn, 3.0% Ag, 0.5% Cu) lead-free alloy solder paste. The thermal profile in the multi-zone reflow convection oven ramps through preheating (150°C to 200°C) to a peak temperature of 240°C to 250°C, held above liquidus (217°C) for 60 to 90 seconds.",
            "doc_hi": "पर्यावरण के अनुकूल लीड-फ्री सोल्डरिंग (SAC305) के लिए अधिकतम तापमान 240°C से 250°C तक पहुंचना चाहिए और इसे 60 से 90 सेकंड के लिए बनाए रखा जाता है।",
            "doc_te": "సీసం లేని పర్యావరణ అనుకూల ఎలక్ట్రానిక్స్ (SAC305) తయారీలో సర్క్యూట్ బోర్డుల సోల్డరింగ్ కొరకు ఓవెన్‌లో గరిష్ట ఉష్ణోగ్రత 240°C నుండి 250°C మధ్య ఉండాలి మరియు దీనిని 60 నుండి 90 సెకన్ల పాటు నిర్వహించాలి.",
            "doc_teen": "RoHS compliant lead-free SAC305 SMT reflow profile lo peak convection oven temperature 240°C to 250°C reach avtundi, with time above liquidus (217°C) held between 60 to 90 seconds."
        },
        {
            "topic": "Electrostatic Discharge ESD Workstation Testing",
            "task_en": "What electrical resistance to ground must an ESD-safe wrist strap maintain during daily testing?",
            "task_hi": "दैनिक परीक्षण के दौरान ईएसडी-सुरक्षित रिस्ट स्ट्रैप को ग्राउंड से कितना विद्युत प्रतिरोध बनाए रखना चाहिए?",
            "task_te": "ఎలక్ట్రానిక్స్ అసెంబ్లీలో వాడే ఈఎస్‌డీ (ESD) రిస్ట్ బ్యాండ్‌కు గ్రౌండ్‌తో ఉండే సరైన రెసిస్టెన్స్ ఎంత?",
            "task_teen": "ESD workstation safety compliance lo wrist strap resistance to ground daily tester rating entha?",
            "doc_en": "Electronics manufacturing workstations assembling sensitive MOSFET semiconductors require strict Electrostatic Discharge (ESD) controls compliant with ANSI/ESD S20.20. Personnel must test wrist straps daily on calibrated continuous ground testers. A compliant strap must exhibit a total system resistance to ground between 0.8 Megohms and 1.2 Megohms (nominally 1.0 Megohm) to dissipate static safely.",
            "doc_hi": "संवेदनशील चिप्स को नुकसान से बचाने के लिए, ईएसडी रिस्ट स्ट्रैप का ग्राउंड प्रतिरोध 0.8 से 1.2 मेगाओम (Megohms) के बीच होना चाहिए। इसका प्रतिदिन परीक्षण किया जाना चाहिए।",
            "doc_te": "ఎలక్ట్రానిక్ చిప్స్ తయారీలో స్టాటిక్ విద్యుత్ వల్ల చిప్స్ పాడవకుండా ఉండటానికి ఆపరేటర్లు చేతికి ESD రిస్ట్ బ్యాండ్ ధరిస్తారు. దీని విద్యుత్ నిరోధకత (రెసిస్టెన్స్) గ్రౌండ్‌తో 0.8 నుండి 1.2 మెగాఓమ్స్ మధ్య ఉండేలా ప్రతిరోజూ పరీక్షించాలి.",
            "doc_teen": "ANSI/ESD S20.20 electronics assembly standard prakaram ESD wrist strap resistance to ground nominally 1.0 Megohm (0.8 to 1.2 Megohms range) undali to discharge static electricity safely."
        },
        {
            "topic": "USB 2.0 Differential Pair Routing Impedance",
            "task_en": "What target differential trace impedance is required when routing high-speed USB 2.0 data pairs on a PCB?",
            "task_hi": "पीसीबी पर यूएसबी 2.0 डेटा लाइनों को रूट करते समय कौन सा डिफरेंशियल इम्पीडेंस आवश्यक है?",
            "task_te": "సర్క్యూట్ బోర్డుపై హై-స్పీడ్ USB 2.0 లైన్లను డిజైన్ చేసేటప్పుడు ఎంత డిఫరెన్షియల్ ఇంపెడెన్స్ ఉండాలి?",
            "task_teen": "PCB layout lo high-speed USB 2.0 D+ and D- differential pair target impedance entha?",
            "doc_en": "Printed circuit board (PCB) layout design guidelines for High-Speed (480 Mbps) USB 2.0 data buses require differential routing for the complementary D+ and D- trace pair. The layout designer must configure trace geometry and dielectric substrate spacing to achieve a continuous differential impedance of exactly 90 Ohms +/- 10%, tightly length-matched within 1.25 mm to prevent phase skew.",
            "doc_hi": "हाई-स्पीड यूएसबी 2.0 डेटा लाइनों (D+ और D-) के लिए पीसीबी पर 90 ओम (+/- 10%) का निरंतर डिफरेंशियल इम्पीडेंस होना चाहिए ताकि सिग्नल में कोई त्रुटि न आए।",
            "doc_te": "సర్క్యూట్ బోర్డు (PCB) పై 480 Mbps వేగంతో పనిచేసే USB 2.0 డేటా లైన్లను డిజైన్ చేసేటప్పుడు డిఫరెన్షియల్ ఇంపెడెన్స్ ఖచ్చితంగా 90 Ohms (+/- 10%) ఉండేలా చూడాలి, లేకుంటే డేటా ప్రసారంలో లోపాలు ఏర్పడతాయి.",
            "doc_teen": "High-Speed USB 2.0 differential pair (D+/D-) routing lo PCB trace impedance continuous ga exactly 90 Ohms +/- 10% maintain cheyali with tight length matching within 1.25 mm."
        },
        {
            "topic": "EEPROM Wear-Leveling Algorithm Lifespan",
            "task_en": "Why do embedded systems utilize wear-leveling algorithms when writing configuration data to EEPROM or flash?",
            "task_hi": "ईईपीआरओएम या फ्लैश में डेटा लिखते समय एम्बेडेड सिस्टम वियर-लेवलिंग एल्गोरिदम का उपयोग क्यों करते हैं?",
            "task_te": "మైక్రోకంట్రోలర్లలో సమాచారాన్ని నిల్వ చేసేటప్పుడు వేర్-లెవలింగ్ (Wear-leveling) విధానాన్ని ఎందుకు ఉపయోగిస్తారు?",
            "task_teen": "Embedded systems EEPROM mariyu flash storage lo wear-leveling algorithms enduku deploy chesthayi?",
            "doc_en": "Non-volatile EEPROM and NOR flash memory sectors have a finite endurance write lifespan, typically rated at 100,000 write-erase cycles before floating-gate oxide breakdown. Firmware utilizes cyclical wear-leveling algorithms to distribute frequent configuration writes evenly across all memory memory sectors rather than repeatedly stressing a single physical sector, extending flash hardware longevity.",
            "doc_hi": "फ्लैश मेमोरी में केवल 100,000 बार लिखने की क्षमता होती है। वियर-लेवलिंग एल्गोरिदम डेटा को सभी सेक्टरों में समान रूप से फैलाता है ताकि कोई एक सेक्टर जल्दी खराब न हो।",
            "doc_te": "ఫ్లాష్ మెమరీలో డేటాను గరిష్టంగా 100,000 సార్లు మాత్రమే తిరిగి రాయవచ్చు (ఎరేజ్ చేయవచ్చు). వేర్-లెవలింగ్ సాఫ్ట్‌వేర్ పదేపదే ఒకే మెమరీ ప్రాంతంపై డేటా రాయకుండా అన్ని బ్లాక్‌లలో సమానంగా సమాచారాన్ని పంపిణీ చేసి మెమరీ జీవితకాలాన్ని పెంచుతుంది.",
            "doc_teen": "Flash EEPROM cells ki 100,000 write-erase endurance cycles matrame untayi. Wear-leveling algorithms writes ni memory blocks antha evenly distribute chesi single sector degradation prevent chesthayi."
        },
        {
            "topic": "Hardware Watchdog Timer Reset Interval",
            "task_en": "How does an independent hardware watchdog timer recover microcontrollers from infinite software loops?",
            "task_hi": "हार्डवेयर वॉचडॉग टाइमर माइक्रोकंट्रोलर को सॉफ्टवेयर हैंग होने से कैसे बचाता है?",
            "task_te": "సాఫ్ట్‌వేర్ హ్యాంగ్ అయినప్పుడు హార్డ్‌వేర్ వాచ్‌డాగ్ టైమర్ మైక్రోకంట్రోలర్‌ను ఎలా రీస్టార్ట్ చేస్తుంది?",
            "task_teen": "Independent hardware watchdog timer microcontroller software crash nunchi ela recover chesthundi?",
            "doc_en": "Embedded firmware employs an autonomous hardware watchdog timer (WDT) clocked by an independent RC oscillator. The main firmware execution loop must periodically 'pet' or reset the timer before its countdown window (e.g., 2.0 seconds) expires. If software hangs in an unhandled deadlock or infinite loop, the timer underflows, asserting an automated hardware reset pulse that reboots the MCU.",
            "doc_hi": "वॉचडॉग टाइमर एक सुरक्षा तंत्र है। यदि मुख्य प्रोग्राम क्रैश हो जाता है या हैंग हो जाता है, तो टाइमर समाप्त हो जाता है और माइक्रोकंट्रोलर को स्वचालित रूप से पुनरारंभ (Reboot) कर देता है।",
            "doc_te": "సాఫ్ట్‌వేర్ హ్యాంగ్ అయినప్పుడు లేదా నిరంతర లూప్‌లో చిక్కుకున్నప్పుడు వాచ్‌డాగ్ టైమర్ రక్షణ కల్పిస్తుంది. ప్రోగ్రామ్ నుండి నిర్ణీత సమయంలో (ఉదా. 2 సెకన్లు) సిగ్నల్ రాకపోతే, ఈ టైమర్ మైక్రోకంట్రోలర్‌ను ఆటోమేటిక్‌గా రీబూట్ చేస్తుంది.",
            "doc_teen": "Independent hardware watchdog timer (WDT) countdown timer run chesthundi. Main loop 2.0 seconds lopala timer refresh cheyakapothe (crash or deadlock valla) MCU automated hardware reset assert ayyi reboot avtundi."
        }
    ]
}

# Domain 23: Environmental & Climate Monitoring (S221 - S230)
D23 = {
    "domain": "environmental_climate",
    "scenarios": [
        {
            "topic": "Air Quality Index PM2.5 Unhealthy Threshold",
            "task_en": "What 24-hour average concentration of PM2.5 particulate matter triggers an Unhealthy Air Quality Index category?",
            "task_hi": "PM2.5 की कौन सी सांद्रता अस्वास्थ्यकर (Unhealthy) वायु गुणवत्ता सूचकांक को ट्रिगर करती है?",
            "task_te": "గాలిలోని PM2.5 ధూళి కణాల సాంద్రత ఎంత దాటితే గాలి నాణ్యత సూచీ (AQI) ప్రమాదకర స్థాయికి చేరుతుంది?",
            "task_teen": "Air Quality Index (AQI) lo PM2.5 24-hour concentration entha unte 'Unhealthy' category trigger avtundi?",
            "doc_en": "Environmental protection ambient air quality monitoring standards classify air quality across six standardized Air Quality Index (AQI) categories. A 24-hour mean fine particulate matter (PM2.5) atmospheric concentration between 55.5 and 150.4 micrograms per cubic meter (ug/m3) triggers an 'Unhealthy' AQI rating (AQI 151 to 200), necessitating public health advisories to avoid outdoor physical exertion.",
            "doc_hi": "यदि 24 घंटे में हवा में PM2.5 की सांद्रता 55.5 से 150.4 माइक्रोग्राम प्रति क्यूबिक मीटर के बीच होती है, तो वायु गुणवत्ता 'अस्वास्थ्यकर' (Unhealthy) मानी जाती है और बाहर जाने से बचने की सलाह दी जाती है।",
            "doc_te": "పర్యావరణ శాఖ ప్రమాణాల ప్రకారం గాలిలోని అతి సూక్ష్మ కణాలు (PM2.5) ఒక క్యూబిక్ మీటరుకు 55.5 నుండి 150.4 మైక్రోగ్రాములు దాటితే గాలి నాణ్యత 'అనారోగ్యకరమైనది' (Unhealthy) గా ప్రకటించబడుతుంది మరియు ప్రజలు బయటకు రావద్దని హెచ్చరిస్తారు.",
            "doc_teen": "Air quality monitoring standards prakaram 24-hour mean PM2.5 concentration 55.5 to 150.4 ug/m3 unte 'Unhealthy' AQI (151 to 200) trigger avtundi requiring public health warnings."
        },
        {
            "topic": "Industrial Wastewater Effluent pH Discharge Standards",
            "task_en": "What permissible pH range is mandated for industrial wastewater effluent discharged into public waterways?",
            "task_hi": "सार्वजनिक जलमार्गों में छोड़े जाने वाले औद्योगिक अपशिष्ट जल के लिए अनुमत pH सीमा क्या है?",
            "task_te": "నదుల్లోకి వదిలే పారిశ్రామిక వ్యర్థ జలాల యొక్క pH విలువ ఏ పరిధిలో ఉండటం చట్టరీత్యా తప్పనిసరి?",
            "task_teen": "Industrial wastewater effluent river discharge chesetappudu mandatory permissible pH range entha?",
            "doc_en": "Under clean water statutory environmental protection acts, treated industrial trade effluent discharged from chemical, textile, and manufacturing plants into inland surface waterways must strictly maintain a neutral pH between 6.5 and 8.5. Effluent streams with acidic pH below 6.5 or alkaline pH exceeding 8.5 are subject to severe civil environmental fines and plant operational closure.",
            "doc_hi": "पर्यावरण कानूनों के तहत, नदियों में छोड़े जाने वाले औद्योगिक अपशिष्ट जल का pH मान 6.5 और 8.5 के बीच होना चाहिए। इस सीमा का उल्लंघन करने पर भारी जुर्माना लगाया जाता है।",
            "doc_te": "కాలుష్య నియంత్రణ చట్టాల ప్రకారం పరిశ్రమల నుండి నదుల్లోకి మరియు కాలువల్లోకి వదిలే వ్యర్థ జలాల యొక్క pH విలువ ఖచ్చితంగా 6.5 నుండి 8.5 మధ్య తటస్థంగా ఉండాలి. ఆమ్లత్వం లేదా క్షారత్వం ఎక్కువగా ఉన్న నీటిని వదిలితే ఫ్యాక్టరీలను మూసివేయిస్తారు.",
            "doc_teen": "Clean water environmental regulations prakaram treated industrial trade effluent inland waterways ki discharge cheyali ante pH strictly 6.5 to 8.5 neutral range maintain cheyali."
        },
        {
            "topic": "Authorized E-Waste Precious Metal Recovery",
            "task_en": "What closed-loop recovery methods are certified for extracting gold and copper from commercial electronic waste?",
            "task_hi": "इलेक्ट्रॉनिक कचरे से सोना और तांबा निकालने के लिए कौन सी प्रमाणित विधियां हैं?",
            "task_te": "ఎలక్ట్రానిక్ వ్యర్థాల (ఈ-వేస్ట్) నుండి బంగారం మరియు రాగిని వెలికితీయడానికి ఏ పద్ధతులను అనుమతిస్తారు?",
            "task_teen": "E-waste recycling facilities lo precious metals (gold, copper) recovery kosam certified eco-friendly methods emiti?",
            "doc_en": "State hazardous electronic waste management rules require printed circuit boards (PCBs) to be processed exclusively in certified, authorized recycling facilities employing closed-loop hydrometallurgical leaching or automated pyrometallurgical smelting with acid-gas scrubbers. Crude open-air acid bath washing and open burning of cable insulation are strictly criminalized.",
            "doc_hi": "ई-कचरे से सोना और तांबा निकालने के लिए केवल अधिकृत कारखानों में रासायनिक लीचिंग विधियों की अनुमति है। खुले में एसिड से धोना या तारों को जलाना कानूनी रूप से अपराध है।",
            "doc_te": "ఈ-వేస్ట్ రీసైక్లింగ్ నిబంధనల ప్రకారం సర్క్యూట్ బోర్డుల నుండి విలువైన లోహాలను తీయడానికి కేవలం అధీకృత కేంద్రాలలో క్లోజ్డ్ కెమికల్ లీచింగ్ లేదా స్మెల్టింగ్ పద్ధతులను మాత్రమే వాడాలి. బహిరంగ ప్రదేశాల్లో యాసిడ్ వాడటం లేదా వైర్లను కాల్చడం చట్టరీత్యా నేరం.",
            "doc_teen": "E-waste regulations prakaram printed circuit boards nunchi precious metals recover cheyali ante authorized facilities lo closed-loop hydrometallurgical leaching use cheyali; open-air burning criminal offence."
        },
        {
            "topic": "Commercial Groundwater Extraction Flow Metering",
            "task_en": "What volumetric extraction limit and metering hardware are mandatory for commercial borehole groundwater permits?",
            "task_hi": "वाणिज्यिक भूजल निष्कर्षण परमिट के लिए क्या सीमा और मीटरिंग हार्डवेयर अनिवार्य है?",
            "task_te": "వాణిజ్య అవసరాల కోసం భూగర్భ జలాలను తోడుకోవడానికి అనుమతించబడిన పరిమితి మరియు మీటరింగ్ నిబంధన ఏమిటి?",
            "task_teen": "Commercial borehole groundwater extraction permit lo volumetric daily cap mariyu metering hardware emiti?",
            "doc_en": "National water resources authority guidelines mandate that commercial and industrial facilities extracting groundwater via deep borewells must install automated, tamper-proof ultrasonic digital flow meters equipped with telemetry transmitters. Daily abstraction is capped by permit conditions (typically 50,000 liters/day in semi-critical basins) to prevent aquifer depletion.",
            "doc_hi": "भूजल निकालने वाले कारखानों को डिजिटल फ्लो मीटर लगाना अनिवार्य है। भूजल स्तर को बचाने के लिए प्रतिदिन 50,000 लीटर तक पानी निकालने की सीमा तय की गई है।",
            "doc_te": "భూగర్భ జలాల పరిరక్షణ చట్టం ప్రకారం బోర్‌వెల్స్ ద్వారా నీటిని తోడే పరిశ్రమలు తప్పనిసరిగా డిజిటల్ ఫ్లో మీటర్లను ఏర్పాటు చేసుకోవాలి. భూగర్భ జలాలు అడుగంటిపోకుండా ఉండటానికి రోజుకు గరిష్టంగా 50,000 లీటర్ల పరిమితిని విధిస్తారు.",
            "doc_teen": "Groundwater extraction permits prakaram industrial facilities automated digital ultrasonic flow meters install cheyali with telemetry. Aquifer depletion prevent cheyadaniki daily cap 50,000 liters/day fix chestharu."
        },
        {
            "topic": "Industrial Perimeter Ambient Noise Standards",
            "task_en": "What are the daytime and nighttime ambient noise decibel limits at industrial zone boundary perimeters?",
            "task_hi": "औद्योगिक क्षेत्र की सीमाओं पर दिन और रात के लिए ध्वनि डेसिबल सीमाएं क्या हैं?",
            "task_te": "పారిశ్రామిక ప్రాంతాల సరిహద్దుల వద్ద పగలు మరియు రాత్రి సమయాల్లో అనుమతించబడే శబ్ద తీవ్రత పరిమితులు ఏమిటి?",
            "task_teen": "Industrial zone boundary perimeter lo permissible daytime mariyu nighttime ambient noise decibels entha?",
            "doc_en": "Environmental noise pollution regulation rules specify permissible equivalent continuous sound pressure levels (Leq) at the boundary perimeters of designated industrial zones. The daytime ambient noise limit (measured between 6:00 AM and 10:00 PM) is set at 75 dBA Leq, whereas nighttime ambient emissions (10:00 PM to 6:00 AM) must drop to or below 70 dBA Leq.",
            "doc_hi": "औद्योगिक क्षेत्रों में दिन के समय (सुबह 6:00 से रात 10:00 बजे तक) ध्वनि स्तर 75 dBA और रात के समय 70 dBA से कम होना चाहिए।",
            "doc_te": "శబ్ద కాలుష్య నియంత్రణ నిబంధనల ప్రకారం పరిశ్రమల సరిహద్దుల వద్ద పగటిపూట (ఉదయం 6:00 నుండి రాత్రి 10:00 వరకు) శబ్ద తీవ్రత 75 dBA మరియు రాత్రిపూట 70 dBA మించకూడదు.",
            "doc_teen": "Environmental noise pollution rules prakaram industrial zone boundary daggara daytime (6 AM to 10 PM) limit 75 dBA Leq mariyu nighttime limit 70 dBA Leq strictly maintain cheyali."
        },
        {
            "topic": "Carbon Offset Additionality Verification",
            "task_en": "What fundamental criterion must a forestry or renewable project demonstrate to qualify for certified carbon offset credits?",
            "task_hi": "कार्बन ऑफसेट क्रेडिट के लिए पात्र होने के लिए एक परियोजना को कौन सा मानदंड प्रदर्शित करना होगा?",
            "task_te": "కార్బన్ క్రెడిట్స్ పొందడానికి అటవీ లేదా పునరుత్పాదక ఇంధన ప్రాజెక్టులు ఏ ప్రాథమిక నిబంధనను నిరూపించుకోవాలి?",
            "task_teen": "Certified carbon offset credits verify avvali ante environmental project ae additionality criteria demonstrate cheyali?",
            "doc_en": "Voluntary carbon market certification standards (such as Gold Standard and Verra VCS) require emission reduction projects to definitively demonstrate 'Additionality'. The project sponsor must substantiate that the greenhouse gas reduction or carbon sequestration would not have occurred under a business-as-usual scenario in the absence of carbon credit financing incentives.",
            "doc_hi": "कार्बन क्रेडिट प्राप्त करने के लिए परियोजनाओं को 'अतिरिक्तता' (Additionality) साबित करनी होगी, जिसका अर्थ है कि कार्बन क्रेडिट के बिना यह पर्यावरणीय लाभ संभव नहीं होता।",
            "doc_te": "అంతర్జాతీయ కార్బన్ క్రెడిట్ నిబంధనల ప్రకారం ఏదైనా ప్రాజెక్ట్ కార్బన్ క్రెడిట్లు పొందాలంటే 'ఎడిషనాలిటీ'ని నిరూపించుకోవాలి. అంటే కార్బన్ క్రెడిట్స్ ప్రోత్సాహం లేకపోతే ఆ ప్రాజెక్ట్ ద్వారా పర్యావరణానికి లభించిన ఈ అదనపు ప్రయోజనం సహజంగా సాధ్యమయ్యేది కాదని రుజువు చేయాలి.",
            "doc_teen": "Carbon credit certification standards (Verra, Gold Standard) lo 'Additionality' proof compulsory: project greenhouse gas reduction carbon financing incentives lekunda business-as-usual lo occur ayyedi kadani verify cheyali."
        },
        {
            "topic": "Rigid Polymer Plastic Recycling Classifications",
            "task_en": "What resin identification codes differentiate PET (Type 1) from HDPE (Type 2) plastics?",
            "task_hi": "पीईटी (टाइप 1) और एचडीपीई (टाइप 2) प्लास्टिक को कौन से रेजिन कोड अलग करते हैं?",
            "task_te": "ప్లాస్టిక్ రీసైక్లింగ్‌లో PET (టైప్ 1) మరియు HDPE (టైప్ 2) ప్లాస్టిక్‌లను ఎలా గుర్తిస్తారు?",
            "task_teen": "Plastic container recycling identification lo PET (Type 1) mariyu HDPE (Type 2) resin codes emiti?",
            "doc_en": "Municipal solid waste recycling systems utilize standardized ASTM Resin Identification Codes stamped inside chasing arrow symbols. Type 1 represents Polyethylene Terephthalate (PET/PETE), commonly utilized in transparent beverage bottles. Type 2 represents High-Density Polyethylene (HDPE), characterized by opaque, chemical-resistant polymers utilized in milk jugs and detergent containers.",
            "doc_hi": "प्लास्टिक की बोतलों पर बने त्रिकोण में '1' पीईटी (PET) को दर्शाता है जो पेय की बोतलों में उपयोग होता है, जबकि '2' एचडीपीई (HDPE) को दर्शाता है जो दूध के डिब्बे और डिटर्जेंट की बोतलों में उपयोग होता है।",
            "doc_te": "ప్లాస్టిక్ రీసైక్లింగ్ కొరకు డబ్బాల కింద ముద్రించే త్రిభుజం గుర్తులో '1' ఉంటే అది పానీయాల సీసాలలో వాడే PET ప్లాస్టిక్. '2' ఉంటే అది పాల డబ్బాలు మరియు డిటర్జెంట్ డబ్బాలలో వాడే దృఢమైన HDPE ప్లాస్టిక్.",
            "doc_teen": "Resin Identification Codes lo chasing arrows madhyalo '1' unte Polyethylene Terephthalate (PET) beverage bottles, mariyu '2' unte High-Density Polyethylene (HDPE) milk and detergent jugs."
        },
        {
            "topic": "Mandatory Commercial Rainwater Harvesting Storage",
            "task_en": "What minimum rainwater runoff collection capacity is mandatory for commercial buildings exceeding 500 square meters?",
            "task_hi": "500 वर्ग मीटर से अधिक की व्यावसायिक इमारतों के लिए वर्षा जल संचयन की क्या क्षमता अनिवार्य है?",
            "task_te": "500 చదరపు మీటర్ల కంటే పెద్ద వాణిజ్య భవనాలకు వర్షపు నీటి నిల్వ (రెయిన్‌వాటర్ హార్వెస్టింగ్) ఎంత సామర్థ్యం కలిగి ఉండాలి?",
            "task_teen": "Commercial buildings 500 sq meters daatithe rainwater harvesting storage capacity minimum entha undali?",
            "doc_en": "Municipal building bylaws require all commercial complexes with roof catchment footprints exceeding 500 square meters to construct dedicated rainwater harvesting storage cisterns and groundwater percolation pits. Storage reservoirs must be engineered to capture at least 60 days of rainfall runoff based on historical precipitation averages, reducing municipal stormwater surges.",
            "doc_hi": "500 वर्ग मीटर से बड़ी इमारतों के लिए वर्षा जल संचयन अनिवार्य है। जलाशयों को कम से कम 60 दिनों के वर्षा जल को संग्रहीत करने के लिए डिज़ाइन किया जाना चाहिए।",
            "doc_te": "భవన నిర్మాణ నిబంధనల ప్రకారం 500 చదరపు మీటర్ల కంటే ఎక్కువ విస్తీర్ణం కలిగిన వాణిజ్య భవనాలు వర్షపు నీటి నిల్వ సంపులను మరియు ఇంకుడు గుంతలను నిర్మించాలి. కనీసం 60 రోజుల వర్షపు నీటిని నిల్వ చేసే సామర్థ్యం ఉండటం తప్పనిసరి.",
            "doc_teen": "Municipal building codes prakaram 500 sq meters kante pedda commercial buildings lo dedicated rainwater harvesting storage tanks construct cheyali to capture at least 60 days of rainfall runoff."
        },
        {
            "topic": "Hazardous Waste Manifest Tracking Form 10",
            "task_en": "What document accompanies off-site road shipments of hazardous industrial waste to authorized treatment facilities?",
            "task_hi": "खतरनाक औद्योगिक कचरे के परिवहन के साथ कौन सा दस्तावेज होना अनिवार्य है?",
            "task_te": "ప్రమాదకర పారిశ్రామిక వ్యర్థాలను శుద్ధి కేంద్రాలకు తరలించేటప్పుడు వాహనంలో ఏ అధికారిక పత్రం ఉండాలి?",
            "task_teen": "Hazardous industrial waste transport vehicles tho paatu travel chese statutory manifest document emiti?",
            "doc_en": "Statutory hazardous and other waste management rules require that every consignment of toxic industrial waste transported off-site for disposal must be accompanied by a standardized six-copy hazardous waste manifest (Form 10). The color-coded document must be signed by the generator, driver, and disposal operator, tracking waste through complete destruction.",
            "doc_hi": "खतरनाक कचरे के परिवहन के दौरान 'फॉर्म 10' मैनिफेस्ट दस्तावेज का साथ होना अनिवार्य है। यह कचरा उत्पन्न करने वाले, चालक और निस्तारण केंद्र द्वारा हस्ताक्षरित होना चाहिए।",
            "doc_te": "ప్రమాదకర వ్యర్థాల నిర్వహణ చట్టం ప్రకారం ఫ్యాక్టరీల నుండి వ్యర్థాలను తరలించే వాహనంలో ఆరు కాపీల ఫారం 10 మ్యానిఫెస్ట్ పత్రం ఉండటం తప్పనిసరి. వ్యర్థాలను ఉత్పత్తి చేసిన వారు, లారీ డ్రైవర్ మరియు శుద్ధి కేంద్రం అధికారులు దీనిపై సంతకం చేయాలి.",
            "doc_teen": "Hazardous waste management rules prakaram toxic waste transport off-site consignment ki six-copy hazardous waste manifest (Form 10) carry cheyali signed by generator, driver mariyu operator."
        },
        {
            "topic": "Coastal Regulation Zone CRZ Construction Restrictions",
            "task_en": "What construction buffer setback is prohibited from the High Tide Line under Coastal Regulation Zone rules?",
            "task_hi": "तटीय विनियमन क्षेत्र (CRZ) नियमों के तहत हाई टाइड लाइन से कितनी दूरी तक निर्माण प्रतिबंधित है?",
            "task_te": "తీరప్రాంత నియంత్రణ మండలి (CRZ) నిబంధనల ప్రకారం సముద్రపు పోటు గీత (హై టైడ్ లైన్) నుండి ఎన్ని మీటర్ల వరకు నిర్మాణాలు నిషిద్ధం?",
            "task_teen": "Coastal Regulation Zone (CRZ) environmental rules lo High Tide Line nunchi no-construction zone distance entha?",
            "doc_en": "Environmental coastal protection directives delineate sensitive Coastal Regulation Zones (CRZ). Under CRZ-III rural coastal guidelines, a strict No Development Zone (NDZ) extends 200 meters landward from the demarcated High Tide Line (HTL). Permanent commercial hotels, industrial complexes, and residential subdivisions are prohibited within this 200-meter ecological buffer.",
            "doc_hi": "तटीय पर्यावरण नियमों के तहत, हाई टाइड लाइन (HTL) से 200 मीटर तक किसी भी प्रकार के स्थायी निर्माण (होटल, कारखाने या घर) पर सख्त प्रतिबंध है।",
            "doc_te": "తీరప్రాంత పర్యావరణ రక్షణ చట్టం ప్రకారం సముద్రపు ఆటుపోట్ల గీత (హై టైడ్ లైన్) నుండి 200 మీటర్ల పరిధిని 'నో డెవలప్‌మెంట్ జోన్'గా ప్రకటిస్తారు. ఈ 200 మీటర్ల పరిధిలో శాశ్వత హోటళ్లు, ఫ్యాక్టరీలు లేదా నివాసాలు నిర్మించడం చట్టవిరుద్ధం.",
            "doc_teen": "Coastal Regulation Zone (CRZ) rules prakaram High Tide Line (HTL) nunchi 200 meters landward distance strictly No Development Zone (NDZ) ga declare chestharu where commercial constructions are banned."
        }
    ]
}

# Domain 24: Public Health & Disaster Safety (S231 - S240)
D24 = {
    "domain": "public_health_safety",
    "scenarios": [
        {
            "topic": "Epidemic Contact Tracing Quarantine Duration",
            "task_en": "What is the recommended quarantine duration for close contacts exposed to respiratory communicable viral outbreaks?",
            "task_hi": "श्वसन संक्रामक वायरल प्रकोप के संपर्क में आने वाले लोगों के लिए अनुशंसित क्वारंटाइन अवधि क्या है?",
            "task_te": "శ్వాసకోశ అంటువ్యాధులు సోకిన వ్యక్తులతో సన్నిహితంగా ఉన్నవారు ఎన్ని రోజులు క్వారంటైన్‌లో ఉండాలి?",
            "task_teen": "Respiratory viral epidemic contact tracing guidelines lo close contacts quarantine duration enni days?",
            "doc_en": "Epidemiological infectious disease control directives establish containment protocols for acute respiratory viral pandemics. Individuals classified as asymptomatic close contacts (exposed within 6 feet for over 15 cumulative minutes) must maintain home quarantine for 10 calendar days from the date of last exposure, monitoring twice daily for pyrexia or cough.",
            "doc_hi": "संक्रामक बीमारी के संपर्क में आने वाले व्यक्तियों को अंतिम संपर्क की तारीख से 10 दिनों के लिए होम क्वारंटाइन में रहना चाहिए और रोजाना बुखार की निगरानी करनी चाहिए।",
            "doc_te": "అంటువ్యాధుల నియంత్రణ మార్గదర్శకాల ప్రకారం శ్వాసకోశ వైరస్ సోకిన వ్యక్తులతో సన్నిహితంగా మెలిగిన వారు చివరిసారి కలిసిన తేదీ నుండి 10 రోజుల పాటు హోమ్ క్వారంటైన్‌లో ఉండాలి మరియు రోజుకు రెండుసార్లు ఉష్ణోగ్రతను పరీక్షించుకోవాలి.",
            "doc_teen": "Epidemic control protocols prakaram close contacts last exposure date nunchi 10 calendar days home quarantine maintain cheyali monitoring daily body temperature."
        },
        {
            "topic": "Hospital Biomedical Waste Color-Coded Segregation",
            "task_en": "Which color-coded receptacle is prescribed for anatomical human tissue and soiled microbiological waste in hospitals?",
            "task_hi": "अस्पतालों में मानव ऊतकों और सूक्ष्मजीवविज्ञानी कचरे के लिए किस रंग का डस्टबिन निर्धारित है?",
            "task_te": "ఆసుపత్రులలోని బయోమెడికల్ వ్యర్థాల నిర్వహణలో మానవ అవశేషాలు మరియు కణజాలాన్ని ఏ రంగు కవరులో వేయాలి?",
            "task_teen": "Hospital biomedical waste segregation lo anatomical tissues mariyu soiled dressings ae color bin lo dispose cheyali?",
            "doc_en": "Biomedical Waste Management and Handling Rules enforce strict point-of-generation color segregation across all clinical healthcare facilities. Yellow non-chlorinated biohazard plastic bags are exclusively dedicated for anatomical human tissues, amputated organs, placenta, soiled swabs, and infectious microbiological culture media destined for high-temperature incineration.",
            "doc_hi": "अस्पतालों में मानव अंगों, दूषित पट्टियों और संक्रमित ऊतकों को पीले रंग के बायोहाज़र्ड बैग में डालना अनिवार्य है, जिसे बाद में भट्टी में जला दिया जाता है।",
            "doc_te": "బయోమెడికల్ వ్యర్థాల నిర్వహణ నిబంధనల ప్రకారం ఆపరేషన్లలో తొలగించిన శరీర అవయవాలు, రక్తంతో తడిసిన బ్యాండేజీలు మరియు కణజాలాలను పసుపు రంగు (Yellow) బయోహజార్డ్ సంచులలో మాత్రమే వేయాలి, వీటిని ఇంసినరేటర్లలో కాల్చివేస్తారు.",
            "doc_teen": "Biomedical waste management rules prakaram human anatomical tissues, organs mariyu soiled medical cotton yellow color-coded biohazard bags lo matrame dispose cheyali for high-heat incineration."
        },
        {
            "topic": "Municipal Drinking Water Free Chlorine Residual",
            "task_en": "What minimum free residual chlorine concentration must potable tap water maintain at the consumer distribution point?",
            "task_hi": "उपभोक्ता वितरण बिंदु पर पीने के नल के पानी में न्यूनतम क्लोरीन सांद्रता क्या होनी चाहिए?",
            "task_te": "తాగునీటి సరఫరాలో ప్రజల కొళాయిల వద్ద క్లోరిన్ అవశేషాల (ఫ్రీ క్లోరిన్) పరిమాణం ఎంత ఉండాలి?",
            "task_teen": "Potable drinking water consumer distribution tap daggara minimum free residual chlorine concentration entha undali?",
            "doc_en": "Municipal potable water quality and disinfection guidelines adhering to World Health Organization standards require drinking water distributions to maintain continuous bactericidal residual disinfection. Water samples drawn from consumer municipal taps must exhibit a minimum free residual chlorine concentration of 0.2 to 0.5 milligrams per liter (mg/L).",
            "doc_hi": "पीने के पानी में बैक्टीरिया को रोकने के लिए नल के पानी में 0.2 से 0.5 मिलीग्राम प्रति लीटर (mg/L) की अवशिष्ट क्लोरीन सांद्रता होनी चाहिए।",
            "doc_te": "ప్రపంచ ఆరోగ్య సంస్థ ప్రమాణాల ప్రకారం ప్రజలకు సరఫరా చేసే తాగునీటిలో బ్యాక్టీరియా చేరకుండా ఉండేందుకు వినియోగదారుల కొళాయిల వద్ద నీటిలో క్లోరిన్ పరిమాణం కనీసం 0.2 నుండి 0.5 mg/L ఉండటం తప్పనిసరి.",
            "doc_teen": "Potable municipal drinking water standards prakaram consumer distribution taps daggara water-borne bacteria eliminate cheyadaniki free residual chlorine minimum 0.2 to 0.5 mg/L maintain cheyali."
        },
        {
            "topic": "Public Swimming Pool Water Sanitation Chemistry",
            "task_en": "What water pH and free chlorine concentrations must public recreational swimming pools maintain?",
            "task_hi": "सार्वजनिक स्विमिंग पूल में पानी का pH और क्लोरीन का स्तर क्या होना चाहिए?",
            "task_te": "పబ్లిక్ స్విమ్మింగ్ పూల్స్‌లో నీటి యొక్క pH విలువ మరియు క్లోరిన్ పరిమాణం ఎంత ఉండాలి?",
            "task_teen": "Public swimming pool sanitation chemistry lo water pH mariyu free available chlorine ppm levels emiti?",
            "doc_en": "Public aquatic health regulations enforce microbiological sanitation standards across public and commercial recreational swimming facilities. Pool chemistry must be tested every 2 hours to ensure that water pH remains balanced between 7.2 and 7.8, while free available chlorine concentration is continuously maintained between 1.0 and 3.0 parts per million (ppm).",
            "doc_hi": "पब्लिक स्विमिंग पूल में पानी का pH मान 7.2 और 7.8 के बीच और क्लोरीन का स्तर 1.0 से 3.0 पीपीएम (ppm) के बीच होना चाहिए ताकि तैराकों को संक्रमण से बचाया जा सके।",
            "doc_te": "ఈత కొలనులలో అంటువ్యాధులు వ్యాపించకుండా ఉండటానికి నీటి యొక్క pH విలువను 7.2 నుండి 7.8 మధ్య మరియు క్లోరిన్ పరిమాణాన్ని 1.0 నుండి 3.0 ppm మధ్య ఉంచాలి. ప్రతి రెండు గంటలకు నీటిని పరీక్షించడం తప్పనిసరి.",
            "doc_teen": "Public swimming pool sanitation chemistry regulations prakaram water pH 7.2 to 7.8 balanced range lo mariyu free chlorine 1.0 to 3.0 ppm continuous ga maintain cheyali."
        },
        {
            "topic": "Commercial Restaurant Food Hygiene Inspection Scoring",
            "task_en": "What minimum hygiene inspection score out of 100 points earns a commercial restaurant an 'A-Grade' rating?",
            "task_hi": "व्यावसायिक रेस्तरां को 'ए-ग्रेड' रेटिंग प्राप्त करने के लिए 100 में से कितने न्यूनतम स्वच्छता स्कोर की आवश्यकता होती है?",
            "task_te": "హోటళ్లు మరియు రెస్టారెంట్లు 'A-గ్రేడ్' పరిశుభ్రతా సర్టిఫికెట్ పొందడానికి 100కి కనీసం ఎన్ని మార్కులు రావాలి?",
            "task_teen": "Commercial restaurant sanitary food inspection lo 'A-Grade' rating ravali ante score minimum entha undali?",
            "doc_en": "Municipal public health restaurant inspection systems evaluate commercial kitchens across food holding temperatures, cross-contamination prevention, handwashing facilities, and pest abatement. To achieve a premier 'A-Grade' food sanitation placard, an establishment must achieve an inspection score of 90 points or higher out of 100 without any uncorrected critical food safety violations.",
            "doc_hi": "रेस्तरां को 'ए-ग्रेड' स्वच्छता रेटिंग प्राप्त करने के लिए 100 में से कम से कम 90 अंक प्राप्त करने होंगे और कोई गंभीर सुरक्षा उल्लंघन नहीं होना चाहिए।",
            "doc_te": "ఆహార భద్రతా తనిఖీల్లో హోటళ్లు మరియు రెస్టారెంట్లు 'A-గ్రేడ్' రేటింగ్ సాధించాలంటే 100 మార్కులకు కనీసం 90 పాయింట్లు సాధించాలి మరియు ఎలాంటి తీవ్రమైన ఆరోగ్య ఉల్లంఘనలు ఉండకూడదు.",
            "doc_teen": "Public health kitchen inspection lo restaurant 'A-Grade' sanitation placard pondali ante 100 points lo minimum 90 points score cheyali without critical food violations."
        },
        {
            "topic": "Vaccine Cold Chain Temperature Logger Verification",
            "task_en": "How frequently must healthcare clinic personnel physically log vaccine refrigerator storage temperatures?",
            "task_hi": "क्लिनिक कर्मियों को कितनी बार वैक्सीन रेफ्रिजरेटर के तापमान को मैन्युअल रूप से लॉग करना होगा?",
            "task_te": "ఆసుపత్రులలోని వ్యాక్సిన్ ఫ్రిజ్‌ల ఉష్ణోగ్రతను సిబ్బంది రోజుకు ఎన్నిసార్లు రికార్డు పుస్తకంలో నమోదు చేయాలి?",
            "task_teen": "Healthcare clinic staff vaccine storage refrigerator temperatures physical log enni times per day record cheyali?",
            "doc_en": "Centers for Disease Control (CDC) vaccine storage and handling toolkits mandate that designated clinic personnel inspect and manually record vaccine refrigerator temperatures twice daily: once in the morning upon opening and once in the evening before closing. Continuous digital data loggers with buffered temperature probes must confirm the unit remains within 2°C to 8°C.",
            "doc_hi": "क्लिनिक कर्मियों को दिन में दो बार (सुबह और शाम) वैक्सीन फ्रिज के तापमान का निरीक्षण और रिकॉर्ड करना अनिवार्य है ताकि दवाएं सुरक्षित रहें।",
            "doc_te": "వ్యాక్సిన్ల భద్రతా నిబంధనల ప్రకారం క్లినిక్ సిబ్బంది ప్రతిరోజూ ఉదయం మరియు సాయంత్రం రెండుసార్లు ఫ్రిజ్ ఉష్ణోగ్రతను పరిశీలించి రికార్డు బుక్‌లో నమోదు చేయాలి. ఉష్ణోగ్రత ఎల్లప్పుడూ 2°C నుండి 8°C మధ్య ఉండాలి.",
            "doc_teen": "CDC vaccine storage guidelines prakaram clinic staff vaccine refrigerator temperatures ni daily twice (morning mariyu evening) physical log lo verify chesi record cheyali."
        },
        {
            "topic": "Office Workplace Ergonomics Display Monitor Height",
            "task_en": "What is the recommended ergonomic height positioning for computer display monitors relative to seated office workers?",
            "task_hi": "कंप्यूटर डिस्प्ले मॉनिटर के लिए अनुशंसित एर्गोनोमिक ऊंचाई क्या है?",
            "task_te": "కార్యాలయంలో కూర్చుని పనిచేసేటప్పుడు కంప్యూటర్ మానిటర్ యొక్క ఎత్తు ఏ స్థానంలో ఉండాలి?",
            "task_teen": "Office workstation ergonomics lo computer display monitor height positioning recommended rule enti?",
            "doc_en": "Occupational health and ergonomics guidelines for seated VDT office workers state that the top edge of the primary computer display monitor must be positioned at or slightly below eye level (an angle of 15 to 20 degrees below horizontal eye gaze). The screen should be positioned roughly arm's length (20 to 28 inches) from the user's face to reduce neck strain.",
            "doc_hi": "गर्दन के तनाव को कम करने के लिए कंप्यूटर मॉनीटर का शीर्ष किनारा आंखों के स्तर पर या थोड़ा नीचे होना चाहिए और उपयोगकर्ता से 20 से 28 इंच की दूरी पर होना चाहिए।",
            "doc_te": "కార్యాలయాలలో పనిచేసే ఉద్యోగుల మెడ నొప్పులు రాకుండా ఉండటానికి కంప్యూటర్ మానిటర్ పై భాగం కంటి చూపుకు సమానంగా లేదా కొద్దిగా క్రిందకు ఉండాలి. మానిటర్ కళ్ళ నుండి 20 నుండి 28 అంగుళాల దూరంలో ఉండాలి.",
            "doc_teen": "Workplace ergonomics prakaram computer display monitor top edge seated worker eye level daggara kani slightly below undali at 20 to 28 inches viewing distance."
        },
        {
            "topic": "Diagnostic Radiology Medical Staff Dosimeter Badges",
            "task_en": "How frequently are personal thermoluminescent dosimeter (TLD) radiation badges collected from hospital radiology technicians for laboratory readout?",
            "task_hi": "अस्पताल के रेडियोलॉजी कर्मियों से रेडिएशन बैज कितनी बार जांच के लिए एकत्र किए जाते हैं?",
            "task_te": "రేడియాలజీ విభాగంలో పనిచేసే సిబ్బంది ధరించే రేడియేషన్ బ్యాడ్జ్‌లను ఎంత కాలానికి ఒకసారి ల్యాబ్‌లో పరీక్షించి రీడింగ్ తీస్తారు?",
            "task_teen": "Diagnostic radiology medical staff TLD radiation dosimeter badges laboratory readout kosam enni months ki collect chestharu?",
            "doc_en": "Medical radiation safety programs monitoring diagnostic imaging staff operating X-ray, fluoroscopy, and CT scanners mandate that all credentialed radiation workers wear Thermoluminescent Dosimeter (TLD) badges on their chest torso. TLD badges are collected quarterly every 3 months for specialized laboratory processing to track cumulative occupational radiation dose against the 20 mSv annual limit.",
            "doc_hi": "रेडिएशन से जुड़े कर्मचारियों द्वारा पहने जाने वाले टीएलडी बैज हर 3 महीने (तिमाही) में विकिरण के स्तर को मापने और सुरक्षा सुनिश्चित करने के लिए एकत्र किए जाते हैं।",
            "doc_te": "ఎక్స్-రే మరియు CT స్కాన్ విభాగాల సిబ్బంది ధరించే రేడియేషన్ బ్యాడ్జ్‌లను (TLD) ప్రతి 3 నెలలకు ఒకసారి సేకరించి ల్యాబ్‌లో రీడింగ్స్ నమోదు చేస్తారు. ఉద్యోగులపై రేడియేషన్ ప్రభావం వార్షిక పరిమితి అయిన 20 mSv దాటకుండా పర్యవేక్షిస్తారు.",
            "doc_teen": "Hospital radiation safety compliance lo personnel TLD badges quarterly (every 3 months) laboratory processing ki submit chestharu to ensure cumulative dose remains below 20 mSv/year limit."
        },
        {
            "topic": "Industrial Benzene Inhalation Permissible Exposure Limit",
            "task_en": "What is the OSHA Permissible Exposure Limit (PEL) for airborne benzene in petrochemical workplaces?",
            "task_hi": "पेट्रोकेमिकल कार्यस्थलों में बेंजीन के लिए अनुमत जोखिम सीमा (PEL) क्या है?",
            "task_te": "పెట్రోకెమికల్ కర్మాగారాల గాలిలో బెంజీన్ రసాయనం యొక్క గరిష్ట చట్టపరమైన పరిమితి ఎంత?",
            "task_teen": "Petrochemical industry airborne benzene Permissible Exposure Limit (PEL) 8-hour TWA entha?",
            "doc_en": "Occupational Safety and Health Administration (OSHA) health standards strictly regulate occupational exposure to carcinogenic aromatic hydrocarbons. The Permissible Exposure Limit (PEL) for airborne benzene vapor in industrial oil refining and chemical processing facilities is capped at 1.0 part per million (ppm) measured as an 8-hour time-weighted average (TWA), with a short-term limit of 5.0 ppm.",
            "doc_hi": "पेट्रोकेमिकल कारखानों में 8 घंटे के कार्य दिवस के दौरान हवा में बेंजीन का स्तर 1.0 भाग प्रति मिलियन (ppm) से कम होना चाहिए ताकि कैंसर के खतरे को रोका जा सके।",
            "doc_te": "పెట్రోకెమికల్ పరిశ్రమల్లో పనిచేసే కార్మికులు క్యాన్సర్ బారిన పడకుండా గాలిలో బెంజీన్ రసాయన ఆవిరి పరిమాణం 8 గంటల పనివేళల్లో సగటున 1.0 ppm కంటే తక్కువగా ఉండాలని OSHA చట్టం నిర్దేశిస్తుంది.",
            "doc_teen": "OSHA toxic chemical health standards prakaram petrochemical refineries lo airborne benzene Permissible Exposure Limit (PEL) strictly 1.0 ppm 8-hour time-weighted average (TWA) ceiling maintain cheyali."
        },
        {
            "topic": "Urban Extreme Heatwave Wet-Bulb Advisory Trigger",
            "task_en": "What wet-bulb temperature threshold triggers municipal public extreme heat advisories and emergency cooling shelters?",
            "task_hi": "नगर निगम के चरम ताप परामर्श और शीतलन आश्रयों को कौन सा वेट-बल्ब तापमान ट्रिगर करता है?",
            "task_te": "తీవ్రమైన వడగాల్పుల సమయంలో మున్సిపల్ అధికారులు ఏ వెట్-బల్బ్ ఉష్ణోగ్రత వద్ద పబ్లిక్ కూలింగ్ షెల్టర్లను తెరుస్తారు?",
            "task_teen": "Extreme urban heatwave emergency response lo municipal cooling shelters open cheyadaniki wet-bulb temperature trigger entha?",
            "doc_en": "Urban municipal disaster management authorities issue extreme heat public health emergencies when combined atmospheric ambient temperature and relative humidity drive the indoor/outdoor wet-bulb globe temperature (WBGT) above 31°C (88°F). This threshold renders natural human evaporative sweat cooling ineffective, triggering mandatory municipal cooling shelters and construction work stoppages.",
            "doc_hi": "जब वेट-बल्ब तापमान 31°C (88°F) से अधिक हो जाता है, तो नगर निगम आपातकालीन शीतलन आश्रय खोलता है और हीटस्ट्रोक को रोकने के लिए निर्माण कार्य रोक दिया जाता है।",
            "doc_te": "వాతావరణ ఉష్ణోగ్రత మరియు తేమ పెరిగి వెట్-బల్బ్ ఉష్ణోగ్రత 31°C దాటినప్పుడు శరీరం నుండి చెమట ఆరిపోవడం కష్టమవుతుంది. ఈ సమయంలో వడదెబ్బ తగలకుండా ప్రజల కొరకు మున్సిపల్ అధికారులు పబ్లిక్ కూలింగ్ షెల్టర్లను తెరుస్తారు మరియు పనులను ఆపివేయిస్తారు.",
            "doc_teen": "Disaster management authorities wet-bulb temperature (WBGT) 31°C (88°F) exceed ayinappudu extreme heat health emergency declare chesi public cooling shelters open chestharu."
        }
    ]
}

# Domain 25: General Science & Computing (S241 - S250)
D25 = {
    "domain": "general_science",
    "scenarios": [
        {
            "topic": "James Webb Space Telescope Mid-Infrared Mirror Cooling",
            "task_en": "To what cryogenic temperature must the James Webb Space Telescope Mid-Infrared Instrument (MIRI) be cooled?",
            "task_hi": "जेम्स वेब स्पेस टेलीस्कोप के मिड-इन्फ्रारेड उपकरण (MIRI) को किस तापमान तक ठंडा किया जाना चाहिए?",
            "task_te": "జేమ్స్ వెబ్ స్పేస్ టెలిస్కోప్ యొక్క మిడ్-ఇన్‌ఫ్రారెడ్ పరికరాన్ని (MIRI) ఎంత అత్యల్ప ఉష్ణోగ్రత వరకు చల్లబరచాలి?",
            "task_teen": "James Webb Space Telescope Mid-Infrared Instrument (MIRI) cryogenic operational temperature entha?",
            "doc_en": "The James Webb Space Telescope (JWST) operating at the Sun-Earth L2 Lagrange point conducts deep mid-infrared astronomical imaging. While passive sunshields cool the primary observatory to 40 Kelvin (-233°C), the Mid-Infrared Instrument (MIRI) requires active mechanical helium loop cryocooling down to an extreme cryogenic operating temperature of under 7 Kelvin (-266°C).",
            "doc_hi": "जेम्स वेब स्पेस टेलीस्कोप के मिड-इन्फ्रारेड उपकरण (MIRI) को अंतरिक्ष में सटीक छवियों के लिए हीलियम क्रायोकूलर का उपयोग करके 7 केल्विन (-266°C) से कम तापमान तक ठंडा किया जाता है।",
            "doc_te": "జేమ్స్ వెబ్ స్పేస్ టెలిస్కోప్‌లోని మిడ్-ఇన్‌ఫ్రారెడ్ పరికరం (MIRI) అంతరిక్షంలో స్పష్టమైన చిత్రాలను తీయడానికి హీలియం క్రయోకూలర్ ద్వారా అత్యల్పంగా 7 కెల్విన్ల (-266°C) ఉష్ణోగ్రత వరకు చల్లబరచబడుతుంది.",
            "doc_teen": "James Webb Space Telescope deep infrared imaging kosam Mid-Infrared Instrument (MIRI) active closed-cycle helium cryocooler dwara extreme cryogenic operating temperature under 7 Kelvin (-266°C) daggara run avtundi."
        },
        {
            "topic": "Superconducting Quantum Qubit Coherence Times",
            "task_en": "What relaxation coherence time (T1) benchmark characterizes state-of-the-art superconducting transmon qubits?",
            "task_hi": "अत्याधुनिक सुपरकंडक्टिंग ट्रांसमोन क्वबिट्स के लिए रिलैक्सेशन कोहेरेंस समय (T1) क्या है?",
            "task_te": "సూపర్‌కండక్టింగ్ క్వాంటమ్ కంప్యూటర్‌లలోని ట్రాన్స్‌మాన్ క్యూబిట్స్ యొక్క కోహెరెన్స్ సమయం (T1) ఎంత ఉంటుంది?",
            "task_teen": "Superconducting quantum computing transmon qubits lo relaxation coherence time (T1) benchmark entha?",
            "doc_en": "In superconducting quantum computing, quantum processor architectures deploy transmon qubits fabricated from aluminum Josephson junctions cooled to 15 millikelvin inside dilution refrigerators. The benchmark energy relaxation coherence time (T1) for advanced transmon qubits ranges between 100 and 300 microseconds, during which quantum quantum gate operations must execute before decoherence occurs.",
            "doc_hi": "सुपरकंडक्टिंग क्वांटम कंप्यूटरों में ट्रांसमोन क्वबिट्स का कोहेरेंस समय (T1) 100 से 300 माइक्रोसेकंड के बीच होता है, जिसके भीतर त्रुटि होने से पहले कम्प्यूटेशनल ऑपरेशन पूरे होने चाहिए।",
            "doc_te": "సూపర్‌కండక్టింగ్ క్వాంటమ్ కంప్యూటర్లలోని క్యూబిట్లలో సమాచారం చెరిగిపోకుండా ఉండే కోహెరెన్స్ సమయం (T1) సుమారు 100 నుండి 300 మైక్రోసెకన్ల వరకు ఉంటుంది. ఈ స్వల్ప సమయంలోనే క్వాంటమ్ గణనలను పూర్తి చేయాల్సి ఉంటుంది.",
            "doc_teen": "Superconducting quantum processors lo transmon qubits energy relaxation coherence time (T1) 100 to 300 microseconds benchmark maintain chesthayi dilution refrigerators lo at 15 millikelvin."
        },
        {
            "topic": "CRISPR-Cas9 Guide RNA Sequence Length",
            "task_en": "How many nucleotides comprise the target-matching spacer sequence of a single guide RNA in CRISPR-Cas9 genome editing?",
            "task_hi": "CRISPR-Cas9 में गाइड आरएनए (gRNA) के लक्ष्य-मिलान स्पेसर अनुक्रम में कितने न्यूक्लियोटाइड होते हैं?",
            "task_te": "CRISPR-Cas9 జన్యు మార్పిడి సాంకేతికతలో గైడ్ RNA సీక్వెన్స్‌లో ఎన్ని న్యూక్లియోటైడ్లు ఉంటాయి?",
            "task_teen": "CRISPR-Cas9 genome editing target-matching guide RNA (gRNA) spacer sequence lo enni nucleotides untayi?",
            "doc_en": "The bacterial CRISPR-Cas9 molecular genome editing mechanism relies on synthetic single guide RNA (sgRNA) constructs to direct the Cas9 endonuclease enzyme to target genomic DNA loci. The programmable targeting spacer segment of the guide RNA comprises exactly 20 complementary nucleotides positioned immediately adjacent to a 5'-NGG Protospacer Adjacent Motif (PAM).",
            "doc_hi": "CRISPR-Cas9 तकनीक में जीनोम को सटीक रूप से काटने के लिए गाइड आरएनए में लक्ष्य डीएनए से मेल खाने वाले ठीक 20 न्यूक्लियोटाइड होते हैं।",
            "doc_te": "CRISPR-Cas9 జన్యు సవరణ ప్రక్రియలో DNA ను ఖచ్చితమైన ప్రదేశంలో కత్తిరించడానికి ఉపయోగించే గైడ్ RNA లో సరిగ్గా 20 న్యూక్లియోటైడ్ల సీక్వెన్స్ ఉంటుంది. ఇది లక్ష్య జన్యువును గుర్తించి కత్తిరించడానికి ఎంజైమ్‌ను నడిపిస్తుంది.",
            "doc_teen": "CRISPR-Cas9 targeted endonuclease system lo synthetic single guide RNA (sgRNA) targeting spacer segment exactly 20 complementary nucleotides contain chesthundi adjacent to PAM motif."
        },
        {
            "topic": "Seismological Moment Magnitude Earthquake Energy Scale",
            "task_en": "By what factor does radiated seismic wave energy increase for each unit increase in earthquake Moment Magnitude (Mw)?",
            "task_hi": "भूकंप परिमाण (Mw) में प्रत्येक इकाई वृद्धि के लिए भूकंपीय ऊर्जा में कितने गुना वृद्धि होती है?",
            "task_te": "భూకంప తీవ్రత (మోమెంట్ మాగ్నిట్యూడ్ Mw) ఒక పాయింట్ పెరిగినప్పుడు విడుదలయ్యే శక్తి ఎన్ని రెట్లు పెరుగుతుంది?",
            "task_teen": "Earthquake seismology lo Moment Magnitude (Mw) one full unit increase ayithe radiated seismic energy enni times multiply avtundi?",
            "doc_en": "In geophysics and quantitative seismology, earthquake rupture intensity is quantified using the logarithmic Moment Magnitude scale (Mw), determined by the fault slip distance, rupture area, and shear modulus of rock. Because seismic wave radiated energy scales with the 3/2 power of seismic moment, each whole integer increase on the Mw scale corresponds to an approximate 31.6-fold increase in radiated energy.",
            "doc_hi": "भूकंप के परिमाण (Mw) में प्रत्येक 1 अंक की वृद्धि के साथ जारी होने वाली भूकंपीय ऊर्जा में लगभग 31.6 गुना की वृद्धि होती है (जबकि आयाम 10 गुना बढ़ता है)।",
            "doc_te": "భూకంప శాస్త్రం ప్రకారం భూకంప తీవ్రత స్కేల్‌లో ఒక్క పాయింట్ పెరిగితే భూమి లోపలి నుండి విడుదలయ్యే భూకంప తరంగాల శక్తి సుమారు 31.6 రెట్లు పెరుగుతుంది.",
            "doc_teen": "Quantitative seismology Moment Magnitude (Mw) logarithmic scale lo prathi single unit increase radiated seismic energy ni approximately 31.6 times multiply chesthundi."
        },
        {
            "topic": "Relativistic Proton Beam Colliding Energy",
            "task_en": "What is the center-of-mass colliding beam energy achieved by protons at the Large Hadron Collider during Run 3?",
            "task_hi": "लार्ज हैड्रॉन कोलाइडर (LHC) में प्रोटॉन टकराने की ऊर्जा क्या है?",
            "task_te": "లార్జ్ హాడ్రాన్ కొలైడర్ (LHC) లో ప్రోటాన్లు ఢీకొనే గరిష్ట శక్తి (ఎనర్జీ) ఎంత?",
            "task_teen": "Large Hadron Collider (LHC) Run 3 lo relativistic protons center-of-mass colliding beam energy entha?",
            "doc_en": "Particle physics experiments conducted at CERN's Large Hadron Collider (LHC) accelerate dual circulating counter-rotating beams of relativistic protons through a 27-kilometer superconducting vacuum ring. During operational Run 3, superconducting niobium-titanium dipole magnets cooled to 1.9 Kelvin steer protons accelerated to 6.8 Tera-electronvolts (TeV) per beam, yielding a record center-of-mass collision energy of 13.6 TeV.",
            "doc_hi": "सर्न के लार्ज हैड्रॉन कोलाइडर में प्रोटॉन बीम को 6.8 TeV तक त्वरित किया जाता है, जिसके परिणामस्वरूप टकराने पर कुल 13.6 TeV की ऊर्जा उत्पन्न होती है।",
            "doc_te": "యూరప్‌లోని లార్జ్ హాడ్రాన్ కొలైడర్ (LHC) లో ప్రోటాన్లను 27 కిలోమీటర్ల పొడవైన సొరంగంలో కాంతి వేగంతో నడిపిస్తారు. రెండు ప్రోటాన్ కిరణాలు పరస్పరం ఢీకొన్నప్పుడు 13.6 టెరా-ఎలక్ట్రాన్ వోల్ట్ల (13.6 TeV) అపారమైన శక్తి విడుదలవుతుంది.",
            "doc_teen": "CERN Large Hadron Collider (LHC) Run 3 lo counter-rotating proton beams each 6.8 TeV energy achieve chesthayi, resulting in record center-of-mass collision energy of 13.6 TeV."
        },
        {
            "topic": "Solar Flare High-Frequency Radio Blackout Classes",
            "task_en": "Which solar flare classification category triggers severe planetary high-frequency radio blackouts on the sunlit hemisphere?",
            "task_hi": "कौन सा सौर ज्वाला (Solar flare) वर्गीकरण पृथ्वी पर गंभीर रेडियो ब्लैकआउट का कारण बनता है?",
            "task_te": "సూర్యుడి నుండి వెలువడే ఏ తరగతి సౌర జ్వాలలు (సోలార్ ఫ్లేర్స్) భూమిపై రేడియో కమ్యూనికేషన్లను పూర్తిగా స్తంభింపజేస్తాయి?",
            "task_teen": "Solar flare space weather classification lo ae category extreme high-frequency radio blackouts cause chesthundi?",
            "doc_en": "Space weather monitoring observatories classify solar flare energetic X-ray flux into five logarithmic tiers: A, B, C, M, and X. Class X solar flares (peak flux exceeding 10^-4 Watts per square meter at 1 to 8 Angstroms) represent extreme coronal eruptive events that ionize the upper terrestrial ionospheric D-layer, causing total high-frequency (HF) radio communication blackouts across the daylight hemisphere.",
            "doc_hi": "एक्स-क्लास (Class X) सौर ज्वालाएं सबसे शक्तिशाली होती हैं और पृथ्वी के वायुमंडल को प्रभावित करके उच्च-आवृत्ति वाले रेडियो संचार को घंटों तक पूरी तरह से ठप कर सकती हैं।",
            "doc_te": "సౌర తుఫానుల వర్గీకరణలో 'క్లాస్ X' సౌర జ్వాలలు అత్యంత శక్తివంతమైనవి. ఇవి సంభవించినప్పుడు భూమి యొక్క అయానోస్పియర్ ప్రభావితమై విమానాలు మరియు నౌకల హై-ఫ్రీక్వెన్సీ రేడియో సంకేతాలు పూర్తిగా నిలిచిపోతాయి.",
            "doc_teen": "Space weather scales lo Class X solar flares (peak flux exceeding 10^-4 W/m2) extreme ionization cause chesi daylight hemisphere lo total high-frequency (HF) radio blackouts trigger chesthayi."
        },
        {
            "topic": "Historical Ocean Acidification Surface pH Reduction",
            "task_en": "By how much has the average global surface ocean water pH declined since the pre-industrial era?",
            "task_hi": "पूर्व-औद्योगिक काल से अब तक समुद्र की सतह के पानी के औसत pH में कितनी कमी आई है?",
            "task_te": "పారిశ్రామిక విప్లవం ప్రారంభమైనప్పటి నుండి సముద్ర ఉపరితల నీటి యొక్క సగటు pH విలువ ఎంత తగ్గింది?",
            "task_teen": "Pre-industrial era nunchi global ocean surface pH entha decrease ayindi due to ocean acidification?",
            "doc_en": "Marine geochemical climate monitoring quantifies ocean acidification driven by oceanic uptake of anthropogenic carbon dioxide emissions. Since the onset of the pre-industrial era (circa 1750), the mean pH of global surface seawater has decreased from 8.21 down to approximately 8.10. Because pH is measured on a logarithmic scale, this 0.11 unit decline represents an approximate 30% increase in ocean hydrogen ion acidity.",
            "doc_hi": "औद्योगिक क्रांति के बाद से समुद्र के पानी का औसत pH 8.21 से घटकर 8.10 हो गया है। यह 0.11 यूनिट की गिरावट समुद्र की अम्लता में 30% की वृद्धि को दर्शाती है।",
            "doc_te": "పర్యావరణ కాలుష్యం కారణంగా సముద్రపు నీరు ఆమ్లంగా మారుతోంది. పారిశ్రామిక విప్లవానికి ముందు 8.21 గా ఉన్న సముద్ర ఉపరితల pH విలువ ప్రస్తుతం సుమారు 8.10 కి పడిపోయింది, ఇది సముద్ర ఆమ్లత్వంలో 30% పెరుగుదలను సూచిస్తుంది.",
            "doc_teen": "Ocean acidification studies prakaram pre-industrial era nunchi surface seawater mean pH 8.21 nunchi 8.10 ki drop ayindi. Ee 0.11 unit reduction ocean hydrogen ion acidity lo 30% increase ni represent chesthundi."
        },
        {
            "topic": "Gravitational Lensing Dark Matter Galaxy Cluster Mass",
            "task_en": "How does strong gravitational lensing allow astrophysicists to map invisible dark matter distributions in galaxy clusters?",
            "task_hi": "गुरुत्वाकर्षण लेंसिंग (Gravitational lensing) खगोलविदों को डार्क मैटर का नक्शा बनाने की अनुमति कैसे देती है?",
            "task_te": "గెలాక్సీలలో కనిపించని డార్క్ మ్యాటర్ పరిమాణాన్ని గుర్తించడానికి గురుత్వాకర్షణ లెన్సింగ్ సాంకేతికత ఎలా సహాయపడుతుంది?",
            "task_teen": "Strong gravitational lensing observational data astrophysics lo dark matter mapping ki ela use avtundi?",
            "doc_en": "In observational astrophysics, strong gravitational lensing occurs when the immense gravitational field of a massive foreground galaxy cluster warps surrounding spacetime in accordance with General Relativity, deflecting and magnifying light rays from distant background quasars into arcs and multiple images. By analyzing optical distortion angles, astrophysicists reconstruct the invisible dark matter mass profile.",
            "doc_hi": "गुरुत्वाकर्षण लेंसिंग में जब दूर की आकाशगंगाओं से आने वाला प्रकाश डार्क मैटर के भारी गुरुत्वाकर्षण से मुड़ता है, तो खगोलविद उस प्रकाश के मोड़ का विश्लेषण करके अदृश्य डार्क मैटर का नक्शा बनाते हैं।",
            "doc_te": "విశ్వంలో కనిపించని డార్క్ మ్యాటర్‌ను గుర్తించడానికి గురుత్వాకర్షణ లెన్సింగ్ పద్ధతిని వాడతారు. సుదూర గెలాక్సీల నుండి వచ్చే కాంతి డార్క్ మ్యాటర్ గురుత్వాకర్షణ శక్తికి లోబడి వంగి ప్రయాణిస్తుంది, ఆ కాంతి వంపును విశ్లేషించి డార్క్ మ్యాటర్ ఎక్కడెక్కడ ఉందో ఖగోళ శాస్త్రవేత్తలు గుర్తిస్తారు.",
            "doc_teen": "General Relativity prakaram foreground galaxy cluster gravitational field background light ni arc lanti multiple images ga distort chesthundi. Ee optical deflection angles calculate chesi invisible dark matter mass map chestharu."
        },
        {
            "topic": "Exascale Supercomputing Linpack FLOPS Benchmark",
            "task_en": "What computing performance benchmark defines an official 'Exascale' supercomputer on the High Performance Linpack (HPL) test?",
            "task_hi": "हाई परफॉर्मेंस लिनपैक (HPL) परीक्षण पर कौन सा प्रदर्शन एक आधिकारिक 'एक्सास्केल' सुपरकंप्यूटर को परिभाषित करता है?",
            "task_te": "సూపర్‌కంప్యూటర్ల సామర్థ్యాన్ని కొలిచే Linpack పరీక్షలో 'ఎక్సాస్కేల్' హోదా పొందడానికి కనీస వేగం ఎంత ఉండాలి?",
            "task_teen": "High Performance Linpack (HPL) supercomputing benchmark lo official 'Exascale' status qualification rate entha?",
            "doc_en": "Supercomputing architectures are ranked using the standard High Performance Linpack (HPL) benchmark solving dense systems of linear equations. An official 'Exascale' supercomputer achieves sustained 64-bit double-precision floating-point execution speeds exceeding 1.0 ExaFLOPS (10^18 floating-point operations per second or 1,000 PetaFLOPS), utilizing hundreds of thousands of interconnected GPU accelerators.",
            "doc_hi": "एक्सास्केल सुपरकंप्यूटर वह होता है जो प्रति सेकंड 10^18 (एक क्विंटल) फ्लोटिंग-पॉइंट गणनाएं करने में सक्षम होता है। यह 1,000 पेटाफ्लॉप्स से अधिक की गति है।",
            "doc_te": "ప్రపంచంలోని అత్యుత్తమ సూపర్‌కంప్యూటర్లు సెకనుకు 10^18 (ఒక క్వింటిలియన్) ఫ్లోటింగ్ పాయింట్ గణనలను చేసినప్పుడు వాటిని 'ఎక్సాస్కేల్' సూపర్‌కంప్యూటర్లుగా గుర్తిస్తారు. ఇది 1,000 పెటాఫ్లాప్స్ కంటే ఎక్కువ వేగం.",
            "doc_teen": "High Performance Linpack (HPL) benchmark prakaram sustained double-precision compute performance 1.0 ExaFLOPS (10^18 operations per second or 1,000 PetaFLOPS) exceed ayithe official 'Exascale' status qualify avtundi."
        },
        {
            "topic": "Radiocarbon Dating Carbon-14 Radioactive Decay Half-Life",
            "task_en": "What is the radioactive half-life of Carbon-14 utilized in archaeological radiocarbon dating?",
            "task_hi": "पुरातत्व रेडियोकार्बन डेटिंग में उपयोग किए जाने वाले कार्बन-14 का रेडियोधर्मी अर्ध-आयु काल (Half-life) क्या है?",
            "task_te": "పురావస్తు శాస్త్రంలో వస్తువుల కాలాన్ని నిర్ధారించే కార్బన్-14 డేటింగ్‌లో కార్బన్-14 యొక్క అర్ధ జీవిత కాలం (హాఫ్-లైఫ్) ఎంత?",
            "task_teen": "Archaeological radiocarbon dating lo Carbon-14 radioactive decay half-life enni years?",
            "doc_en": "Archaeological and paleontological dating of organic organic matter relies on beta-decay measurement of the unstable radioisotope Carbon-14 (14C). Carbon-14 undergoes decay back into stable Nitrogen-14 with an established physical half-life of 5,730 +/- 40 years. Measuring the remaining ratio of 14C to stable 12C via accelerator mass spectrometry enables accurate dating of artifacts up to 50,000 years old.",
            "doc_hi": "कार्बन-14 का रेडियोधर्मी अर्ध-आयु काल 5,730 वर्ष है। इस पद्धति का उपयोग करके वैज्ञानिक 50,000 वर्ष पुराने तक के कार्बनिक अवशेषों और जीवाश्मों की आयु का सटीक निर्धारण करते हैं।",
            "doc_te": "పురావస్తు తవ్వకాల్లో దొరికిన పురాతన వస్తువుల వయస్సును లెక్కించడానికి కార్బన్-14 డేటింగ్ ఉపయోగిస్తారు. కార్బన్-14 యొక్క అర్ధ జీవిత కాలం 5,730 సంవత్సరాలు. దీని ద్వారా 50,000 సంవత్సరాల నాటి కళాఖండాల వయస్సును ఖచ్చితంగా నిర్ణయించవచ్చు.",
            "doc_teen": "Radiocarbon dating lo radioactive Carbon-14 (14C) decay half-life 5,730 +/- 40 years untundi. Accelerator mass spectrometry dwara remaining 14C/12C ratio measure chesi up to 50,000 years artifacts age date chestharu."
        }
    ]
}

BUILDER5_DOMAINS = [D21, D22, D23, D24, D25]
