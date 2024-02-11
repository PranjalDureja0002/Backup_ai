import re      

def coverage_fields_extractor(text_file_path):

    coverage_sample = {
        "liability_type":"",
        "liability_amount1":"",
        "liability_amount2":"",
        "liability_amount3":"",
        "under_checkbox":"",
        "under_type":"",
        "under_amount1":"",
        "under_amount2":"",
        "under_amount3":"",
        "deductible_checkbox":"",        
        "deductible_amount1":"",
        "deductible_amount2":"",
        "deductible_amount3":"",
        "hired_borrowed_checkbox":"",
        "non_owned_checkbox":""
    }
   

    with open(text_file_path, 'r') as file:
        content = file.readlines()
    
    for i,j in enumerate(content):
        #print(j)
        pattern = "COVERAGES\s+COVERED AUTO SYMBOLS"
        status = ""
        if re.search(pattern,j):
            starting = i
            patt1 = "LIABILITY"
            patt_csl = r"CSL"
            patt_biea = r"BI"
            patt_biea2 = r"EA"

            #status,val = dig_check(content[i],content[i+1],content[i+2],content[i+3])
            
            while ("PHYSICAL DAMAGE" not in content[i] and "TOWING" not in content[i] and "MEDICAL" not in content[i]):             
                        
                #print(content[i])
                if re.search(patt1,content[i]):
                    pos = i
                   
                    while i-pos<10:

                        extracted_item = content[i-5]
                        csl = re.search(patt_csl,extracted_item)
                        bi = re.search(patt_biea,extracted_item)
                        bi2 = re.search(patt_biea2,extracted_item)
                        if csl:
                            
                            span = csl.span()
                            # print("ENTER CSLLLL",content[i-5][span[0]-10:span[0]])
                            if 'X' in content[i-5][span[0]-8:span[0]]:
                                coverage_sample["liability_type"] = "CSL"
                                status = "same"
                                break
                            elif 'X' in content[i-6][span[0]-8:span[0]]:
                                coverage_sample["liability_type"] = "CSL"
                                status = "up"
                                break

                            # print(year)
                            #coverage_sample["liability_type"] = "CSL"
                            
                        if bi:
                            span = bi.span()
                            if 'X' in content[i-5][span[0]-8:span[0]]:
                                coverage_sample["liability_type"] = "BI_EAPER"
                                status = "same"
                                break
                            elif 'X' in content[i-6][span[0]-8:span[0]]:
                                coverage_sample["liability_type"] = "BI_EAPER"
                                status = "up"
                                break
                            elif 'X' in content[i-4][span[0]-8:span[0]]:
                                coverage_sample["liability_type"] = "BI_EAPER"
                                status = "same"
                                break 
                        i+=1
                    break
                i+=1

            i = starting 
            # print("ONEEEEEEEEE",content[i])
            patt1 = "LIABILITY"
            patt_amount = r"\$"
            flag=1
            l1=[]
            while ("PHYSICAL DAMAGE" not in content[i] and "TOWING" not in content[i] and "MEDICAL" not in content[i]):
                if re.search(patt1,content[i]):
                    # print("YYYYY")
                    pos = i
                    while i-pos<10:
                
                        if re.search(patt_amount,content[i-5]):
                            # print("YYYYYY")
                            match = re.search(patt_amount,content[i-5])
                            span = match.span()
                            if status=="same":
                                amount = content[i-5][span[1]:span[1]+40]
                                amount_value = re.findall(r"\s*\d+(?:,\d+)*(?:\.\d+)?\s*",amount)
                                if amount_value:
                                    l1.append("".join(amount_value).strip())
                                else:
                                    l1.append("")
                            elif status=='up':
                                amount = content[i-6][span[1]:span[1]+40]
                                amount_value = re.findall(r"\s*\d+(?:,\d+)*(?:\.\d+)?\s*",amount)
                                if amount_value:
                                    l1.append("".join(amount_value).strip())
                                else:
                                    l1.append("")
                            else:
                                l1.append("")
                            
                        if len(l1)==3:
                            break

                        i+=1

                i+=1
                #print("@@@@@@@",l1)

            coverage_sample["liability_amount1"] = l1[0]
            coverage_sample["liability_amount2"] = l1[1]
            coverage_sample["liability_amount3"] = l1[2]

            # print("OKKKKKKKKKKKk")
            
            i = starting+5
            # print('TWOOOOOO',content[i])
            
            patt2 = "UNINSURED"
            
            patt_csl = r"CSL"
            patt_biea = r"BI"
            patt_biea2 = r"EA"
            while ("HIRED" not in content[i] and "HIRED / BORROWED" not in content[i] and "BORROWED" not in content[i] and 'COST OF HIRE' not in content[i]):
              
                #print(content[i])
                if re.search(patt2,content[i]):
                    pos = i
                   
                    while i-pos<10:

                        extracted_item = content[i-5]
                        csl = re.search(patt_csl,extracted_item)
                        bi = re.search(patt_biea,extracted_item)
                        bi2 = re.search(patt_biea2,extracted_item)
                        if csl:
                            
                            span = csl.span()
                            # print("ENTER CSLLLL",content[i-5][span[0]-10:span[0]])
                            if 'X' in content[i-5][span[0]-8:span[0]]:
                                # print("AAAAAAAAAYAYAYAYA")
                                coverage_sample["under_type"] = "CSL"
                                status = "same"
                                break
                            elif 'X' in content[i-6][span[0]-8:span[0]]:
                                # print("AANANANANANAN")
                                coverage_sample["under_type"] = "CSL"
                                status = "up"
                                break

                            # print(year)
                            #coverage_sample["liability_type"] = "CSL"
                            
                        if bi:
                            # print("PPPPAPAPAPAP")
                            span = bi.span()
                            if 'X' in content[i-5][span[0]-8:span[0]]:
                                coverage_sample["under_type"] = "BI_EAPER"
                                status = "same"
                                break
                            elif 'X' in content[i-6][span[0]-8:span[0]]:
                                coverage_sample["under_type"] = "BI_EAPER"
                                status = "up"
                                break
                            elif 'X' in content[i-4][span[0]-8:span[0]]:
                                coverage_sample["under_type"] = "BI_EAPER"
                                status = "same"
                                break    
                        i+=1
                    break
                i+=1
            # print("THREEEEE",i)

            i = starting + 5
            # print("ONEEEEEEEEE",content[i])
            patt1 = "UNINSURED"
            patt_amount = r"\$"
            flag=1
            l1=[]
            while ("HIRED" not in content[i] and "HIRED / BORROWED" not in content[i] and "BORROWED" not in content[i] and 'COST OF HIRE' not in content[i]):
                if re.search(patt1,content[i]):
                    # print("YYYYY")
                    pos = i
                    while i-pos<10:
                        if re.search(patt_amount,content[i-5]) and 'PERSON' not in content[i-5] and 'CAUSES OF LOSS' not in content[i-5] and 'EXT MED EXP EA PER' not in content[i-5]:
                            # print("YYYYYY")
                            match = re.search(patt_amount,content[i-5])
                            span = match.span()
                            if status=="same":
                                amount = content[i-5][span[1]:span[1]+40]
                                amount_value = re.findall(r"\s*\d+(?:,\d+)*(?:\.\d+)?\s*",amount)
                                if amount_value:
                                    l1.append("".join(amount_value).strip())
                                else:
                                    l1.append("")
                            elif status=='up':
                                amount = content[i-6][span[1]:span[1]+40]
                                amount_value = re.findall(r"\s*\d+(?:,\d+)*(?:\.\d+)?\s*",amount)
                                if amount_value:
                                    l1.append("".join(amount_value).strip())
                                else:
                                    l1.append("")
                            else:
                                l1.append("")
                            
                        if len(l1)==3:
                            break

                        i+=1

                i+=1
                #print("@@@@@@@",l1)

            if len(l1)==2:
                l1.append("")
            if len(l1)==1:
                l1.append("")
                l1.append("")
            coverage_sample["under_amount1"] = l1[0]
            coverage_sample["under_amount2"] = l1[1]
            coverage_sample["under_amount3"] = l1[2]
            i = starting+5
            # print('TWOOOOOO',content[i])
            patt2 = "UNINSURED"
            
            patt_2 = r"2"
            patt_7 = r"7"
            
            while ("HIRED" not in content[i] and "HIRED / BORROWED" not in content[i] and "BORROWED" not in content[i] and 'COST OF HIRE' not in content[i]):
                #print(content[i])
                if re.search(patt2,content[i]):
                    pos = i
                   
                    while i-pos<10:

                        extracted_item = content[i-5]
                        two = re.search(patt_2,extracted_item)
                        seven = re.search(patt_7,extracted_item)
                        
                        if two:
                            span = two.span()
                            # print("ENTER CSLLLL",content[i-5][span[0]-5:span[0]])
                            if 'X' in content[i-5][span[0]-5:span[0]]:
                                # print("AAAAAAAAAYAYAYAYA")
                                coverage_sample["under_checkbox"] = "2"
                                
                                break
                            elif 'X' in content[i-6][span[0]-5:span[0]]:
                                # print("AANANANANANAN")
                                coverage_sample["under_checkbox"] = "2"
                                
                                break

                            # print(year)
                            #coverage_sample["liability_type"] = "CSL"
                            
                        if seven:
                            # print("PPPPAPAPAPAP")
                            span = seven.span()
                            # print("EEEENNENETERSEVENNNN",content[i-5])
                            if 'X' in content[i-5][span[0]-5:span[0]]:
                                coverage_sample["under_checkbox"] = "7"
                                
                                break
                            elif 'X' in content[i-6][span[0]-5:span[0]]:
                                coverage_sample["under_checkbox"] = "7"
                                
                                break
                        i+=1
                    break
                i+=1

            i = starting+5
            # print('TWOOOOOO',content[i])
            
            patt2 = "COVERAGE/DEDUCTIBLE"
            patt2_a = "COVERAGE / DEDUCTIBLE"
            
            patt_var1 = r"COMP"
            patt_var2 = r"OTC"
            patt_2 = r"SPEC"
            patt_3 = r"COLL"
            
            while ("PRIMARY" not in content[i] and "SECONDARY" not in content[i] and "AUTOS" not in content[i]):
                # print(content[i],"AAAAAAAAAA")
                #print(content[i])
                if re.search(patt2,content[i]) or re.search(patt2_a,content[i]):
                    
                    pos = i
                   
                    while i-pos<10:

                        extracted_item = content[i]
                        one_a = re.search(patt_var1,extracted_item)
                        one_b = re.search(patt_var2,extracted_item)
                        two_a = re.search(patt_2,extracted_item)
                        three_a = re.search(patt_3,extracted_item)
                        
                        if one_a or one_b:
                            if one_a:
                                span = one_a.span()
                                # print("ENTER CSLLLL",content[i][span[0]-5:span[0]])
                                if 'X' in content[i][span[0]-5:span[0]]:
                                    
                                    coverage_sample["deductible_checkbox"] = "COMP"
                                    status = "same"
                                    
                                    break
                                elif 'X' in content[i-1][span[0]-5:span[0]]:
                                    # print("AANANANANANAN")
                                    coverage_sample["deductible_checkbox"] = "COMP"
                                    status = "up"
                                    
                                    break
                            else:
                                span = one_b.span()
                                # print("ENTER CSLLLL",content[i][span[0]-5:span[0]])
                                if 'X' in content[i][span[0]-5:span[0]]:
                                    print("AAAAAAAAAYAYAYAYA")
                                    coverage_sample["deductible_checkbox"] = "COMP"
                                    status = "same"
                                    
                                    break
                                elif 'X' in content[i-1][span[0]-5:span[0]]:
                                    # print("AANANANANANAN")
                                    coverage_sample["deductible_checkbox"] = "COMP"
                                    status = "up"
                                    break
                            # print(year)
                            #coverage_sample["liability_type"] = "CSL"
                            
                        if two_a:
                            # print("PPPPAPAPAPAP")
                            span = two_a.span()
                            # print("EEEENNENETERSEVENNNN",content[i])
                            if 'X' in content[i][span[0]-5:span[0]]:
                                coverage_sample["deductible_checkbox"] = "SPEC"
                                status = "same"
                                
                                break
                            elif 'X' in content[i-1][span[0]-5:span[0]] and 'COMP' not in content[i-1] and 'OTC' not in content[i-1]:
                                coverage_sample["deductible_checkbox"] = "SPEC"
                                status = "up"
                                break

                            elif 'X' in content[i+1][span[0]-5:span[0]] and 'COLL' not in content[i+1]:
                                coverage_sample["deductible_checkbox"] = "SPEC"
                                
                                break

                        if three_a:
                            # print("PPPPAPAPAPAP")
                            span = three_a.span()
                            # print("EEEENNENETERSEVENNNN",content[i])
                            if 'X' in content[i][span[0]-5:span[0]]:
                                coverage_sample["deductible_checkbox"] = "COLL"
                                status = "same"
                                break
                            elif 'X' in content[i-1][span[0]-5:span[0]] and 'C OF L' not in content[i-1] and 'SPEC' not in content[i-1]:
                                coverage_sample["deductible_checkbox"] = "COLL"
                                status = "up"
                                break

                            elif 'X' in content[i+1][span[0]-5:span[0]] and 'PRIMARY' not in content[i+1]:
                                coverage_sample["deductible_checkbox"] = "COLL"
                                
                                break
                        i+=1
                    break
                i+=1
            
            i = starting + 5
            # print("ONEEEEEEEEE",content[i])
            patt1 = "COVERAGE/DEDUCTIBLE"
            patt1_a = "COVERAGE / DEDUCTIBLE"
            patt_amount = r"\$"
            flag=1
            l1=[]
            while ("PRIMARY" not in content[i] and "SECONDARY" not in content[i] and "AUTOS" not in content[i]):
                if re.search(patt1,content[i]) or re.search(patt1_a,content[i]):
                    # print("YYYYY")
                    pos = i
                    while i-pos<10:
                

                        if re.search(patt_amount,content[i]) and 'PRIMARY' not in content[i] and 'SECONDARY' not in content[i]:
                            # print("YYYYYY")
                            match = re.search(patt_amount,content[i])
                            span = match.span()
                            if status=="same":
                                amount = content[i][span[1]:]
                                amount_value = re.findall(r"\s*\d+(?:,\d+)*(?:\.\d+)?\s*",amount)
                                if amount_value:
                                    l1.append("".join(amount_value).strip())
                                else:
                                    l1.append("")
                            elif status=='up':
                                amount = content[i-1][span[1]:]
                                amount_value = re.findall(r"\s*\d+(?:,\d+)*(?:\.\d+)?\s*",amount)
                                if amount_value:
                                    l1.append("".join(amount_value).strip())
                                else:
                                    l1.append("")
                            else:
                                l1.append("")
                            
                        if len(l1)==3:
                            break

                        i+=1
                i+=1
                #print("@@@@@@@",l1)

            if len(l1)==2:
                l1.append("")
            if len(l1)==1:
                l1.append("")
                l1.append("")
            coverage_sample["deductible_amount1"] = l1[0]
            coverage_sample["deductible_amount2"] = l1[1]
            coverage_sample["deductible_amount3"] = l1[2]


            i = starting+5
            note_line = 10000
            flag = ""
            # print('TWOOOOOO',content[i])
            
            patt2 = "HIRED/BORROWED|HIRED / BORROWED"
            
            patt_var1 = r"YES"
            patt_var2 = r"NO"
            
            
            while ("NON-OWNED" not in content[i]):
                # print(content[i],"AAAAAAAAAA")
                #print(content[i])
                if re.search(patt2,content[i]):
                    pos = i
                    while i-pos<10:

                        extracted_item = content[i-3]
                        yes = re.search(patt_var1,extracted_item)
                        no = re.search(patt_var2,extracted_item)
                        
                        if flag=="no_seen":
                            break
                        
                        if yes:
                            flag = "yes_seen"
                            # print("PPPPAPAPAPAP")
                            span = yes.span()
                            # print("EEEENNENETERSEVENNNN",content[i])
                            if 'X' in content[i-3][span[0]-5:span[0]]:
                                coverage_sample["hired_borrowed_checkbox"] = "YES"
                                status = "same"
                                note_line = i-3
                                
                                break
                            elif 'X' in content[i-4][span[0]-5:span[0]]:
                                coverage_sample["hired_borrowed_checkbox"] = "YES"
                                status = "up"
                                note_line = i-4
                                break
                        if no:
                            flag = "no_seen"
                            note_line = i-3
                            # print("PPPPAPAPAPAP")
                            span = no.span()
                            # print("EEEENNENETERSEVENNNN",content[i])
                            if 'X' in content[i-3][span[0]-5:span[0]]:
                                coverage_sample["hired_borrowed_checkbox"] = "NO"
                                status = "same"
                                note_line = i-3
                                break
                            elif 'X' in content[i-4][span[0]-5:span[0]]:
                                coverage_sample["hired_borrowed_checkbox"] = "NO"
                                status = "up"
                                note_line = i-4
                                break   
                        i+=1
                    break
                i+=1

            
            i = starting+5
            # print('TWOOOOOO',content[i])
            
            patt2 = "NON-OWNED"
            
            patt_var1 = r"YES"
            patt_var2 = r"NO"
            
            
            while ("AUTOS" not in content[i]):

                # print(content[i],"AAAAAAAAAA")
                #print(content[i])
                if re.search(patt2,content[i]):
                    
                    pos = i
                    while i-pos<10:
                        extracted_item = content[i-5]
                        yes = re.search(patt_var1,extracted_item)
                        no = re.search(patt_var2,extracted_item)

                        #print("XXXXXXXXX",i-3)
                        #print("YYYYYYYYYY",note_line)
                            
                        if yes and (i-5 > note_line):
                            # print("PPPPAPAPAPAP")
                            span = yes.span()
                            #print("EEEENNENETERSEVENNNN",content[i])
                            if 'X' in content[i-5][span[0]-5:span[0]]:
                                # print("OKSWWWWW")
                                coverage_sample["non_owned_checkbox"] = "YES"
                                status = "same"
                                
                                break
                            elif 'X' in content[i-6][span[0]-5:span[0]]:
                                coverage_sample["non_owned_checkbox"] = "YES"
                                status = "up"
                                break
  
                        if no and (i-5 > note_line):
                            # print("PPPPAPAPAPAP")
                            span = no.span()
                            # print("EEEENNENETERSEVENNNN",content[i])
                            if 'X' in content[i-5][span[0]-5:span[0]]:
                                coverage_sample["non_owned_checkbox"] = "NO"
                                status = "same"
                                break
                            elif 'X' in content[i-6][span[0]-5:span[0]]:
                                coverage_sample["non_owned_checkbox"] = "NO"
                                status = "up"
                                break  
                        i+=1
                    break
                i+=1

            break 
    return coverage_sample

#print(coverage_dict)

def main_coverage(file_path):
    coverage_dict = coverage_fields_extractor(file_path)
    coverage_final_dict = {
        "overall":"",
        "deductable":"null",
        "deductableAmount":"null",
        "deductableAutoEntry":"excluded",
        "combinedSectionLimit":"null",
        "combinedSectionEntry":"excluded",
        "splitSectionBodyPerPerson":"null",
        "splitSectionBodyPerAccidentOptions":"null",
        "splitSectionPropertyDamageOptions":"null",
        "splitSectionAutoEntryOptions":"excluded",
        "pIProtectionSingleLimit":"null",             #calibration
        "pIProtectionSingleEntry":"excluded",         #calibration
        "pIProtectionSplitBodyPerPerson":"null",
        "pIProtectionSplitBodyPerAccident":"null",
        "pIProtectionSplitPropertyDamage":"null",
        "pIProtectionSplitAutoEntry":"excluded",
        "pedPipSingleLimit":"",                        #TODO 
        "medicalSingleLimit":"null",
        "medicalSingleEntry":"excluded",
        "medicalSplitBodyPerPerson":"null",
        "medicalSplitBodyPerAccident":"null",
        "medicalSplitPropertyDamage":"null",
        "medicalSplitAutoEntry":"excluded",
        "underinsuredMotoristSingleLimit":"null",                   
        "underinsuredMotoristSingleAutoEntry":"excluded",
        "underMotoristBodyPerPerson":"null",
        "underMotoristBodyPerAccident":"null",
        "underMotoristProperty":"null",
        "underMotoristAuto":"excluded",
        "cslSingleLimit":"null",
        "cslBodyPerAccident":"null",
        "cslBodyPerPerson":"null",
        "cslSingleAuto":"excluded",
        "cslProperty":"null",
        "cslSplitAuto":"excluded",
        "nonCslBodyPerAccident":"null",
        "nonCslBodyPerPerson":"null",
        "nonCslProperty":"null",
        "nonCslSingleAuto":"excluded",
        "nonCslSingleLimit":"null",
        "nonCslSplitAuto":"excluded",
        "unMotoristAuto":"excluded",
        "unMotoristBodyPerAccident":"null",
        "unMotoristBodyPerPerson":"null",
        "unMotoristProperty":"null",
        "uninsuredMotoristSingleAutoEntry":"excluded",
        "uninsuredMotoristSingleLimit":"null",
        "personalInjury":"Combined Section Limit",
        "medicalPayments":"Combined Section Limit",
        "underinsuredMotorist":"null",
        "uninsuredMotorist":"null",
        "csl":"No",
        "nonOwnedCSL":"No",
        "overallPremium":"null",
        "personalInjuryProtectionPremium": "null",
        "pedPipProtectionPremium": "null",
        "medicalPaymentsPremium": "null",
        "underinsuredMotoristPremium":"null",
        "uninsuredMotoristPremium": "null",
        "hiredCSLPremium": "null",
        "nonOwnedCSLPremium": "null"
    } 
    csl_amount = 0
    biea_amount = 0

    if coverage_dict['liability_type'] =='CSL':
        coverage_final_dict['overall'] = 'Combined Single Limit'         #1

        if coverage_dict['liability_amount1'] != "":
            coverage_final_dict['combinedSectionLimit'] = coverage_dict['liability_amount1']
        elif coverage_dict['liability_amount2'] != "":
            coverage_final_dict['combinedSectionLimit'] = coverage_dict['liability_amount2']           #2
        elif coverage_dict['liability_amount3'] != "":
            coverage_final_dict['combinedSectionLimit'] = coverage_dict['liability_amount3']

        csl_amount = int(coverage_final_dict['combinedSectionLimit'].replace(",",""))
        coverage_final_dict['combinedSectionEntry'] = '17'

    elif coverage_dict['liability_type'] =='BI_EAPER':
        coverage_final_dict['overall'] = 'Split Section Limit'         #1

        coverage_final_dict['splitSectionBodyPerPerson'] = coverage_dict['liability_amount1']
        coverage_final_dict['splitSectionBodyPerAccidentOptions'] = coverage_dict['liability_amount2']

        coverage_final_dict['splitSectionPropertyDamageOptions'] = coverage_dict['liability_amount3']

        biea_amount = int(coverage_final_dict['splitSectionBodyPerAccidentOptions'].replace(",",""))
        coverage_final_dict['splitSectionAutoEntryOptions'] = "17"

    if coverage_dict['under_type'] =='CSL':
        coverage_final_dict['underinsuredMotorist'] = "Combined Single Limit"
        coverage_final_dict['uninsuredMotorist'] = "Combined Single Limit"
        if coverage_dict['under_amount1'] != "":
            coverage_final_dict['underinsuredMotoristSingleLimit'] = coverage_dict['under_amount1']
            coverage_final_dict['uninsuredMotoristSingleLimit'] = coverage_dict['under_amount1']
        elif coverage_dict['under_amount2'] != "":
            coverage_final_dict['underinsuredMotoristSingleLimit'] = coverage_dict['under_amount2']   
            coverage_final_dict['uninsuredMotoristSingleLimit'] = coverage_dict['under_amount2']   
        elif coverage_dict['under_amount3'] != "":
            coverage_final_dict['underinsuredMotoristSingleLimit'] = coverage_dict['under_amount3']
            coverage_final_dict['uninsuredMotoristSingleLimit'] = coverage_dict['under_amount3']

        coverage_final_dict['underinsuredMotoristSingleAutoEntry'] = coverage_dict['under_checkbox']
        if coverage_final_dict['underinsuredMotoristSingleAutoEntry'] =='2':
            coverage_final_dict['underinsuredMotoristSingleAutoEntry'] = '12'
        elif coverage_final_dict['underinsuredMotoristSingleAutoEntry'] =='7':
            coverage_final_dict['underinsuredMotoristSingleAutoEntry'] = '17'
        coverage_final_dict['uninsuredMotoristSingleAutoEntry'] = coverage_dict['under_checkbox']
        if coverage_final_dict['uninsuredMotoristSingleAutoEntry'] =='2':
            coverage_final_dict['uninsuredMotoristSingleAutoEntry'] = '12'
        elif coverage_final_dict['uninsuredMotoristSingleAutoEntry'] =='7':
            coverage_final_dict['uninsuredMotoristSingleAutoEntry'] = '17'
    
    elif coverage_dict['under_type'] =='BI_EAPER':

        coverage_final_dict['underinsuredMotorist'] = "Split Section Limit"
        coverage_final_dict['uninsuredMotorist'] = "Split Section Limit"

        coverage_final_dict['underMotoristBodyPerPerson'] = coverage_dict['under_amount1']
        coverage_final_dict['underMotoristBodyPerAccident'] = coverage_dict['under_amount2']
        coverage_final_dict['underMotoristProperty'] = coverage_dict['under_amount3']

        coverage_final_dict['unMotoristBodyPerPerson'] = coverage_dict['under_amount1']
        coverage_final_dict['unMotoristBodyPerAccident'] = coverage_dict['under_amount2']
        coverage_final_dict['unMotoristProperty'] = coverage_dict['under_amount3']

        coverage_final_dict['underMotoristAuto'] = coverage_dict['under_checkbox']
        if coverage_final_dict['underMotoristAuto'] =='2':
            coverage_final_dict['underMotoristAuto'] = '12'
        elif coverage_final_dict['underMotoristAuto'] =='7':
            coverage_final_dict['underMotoristAuto'] = '17'
        coverage_final_dict['unMotoristAuto'] = coverage_dict['under_checkbox']
        if coverage_final_dict['unMotoristAuto'] =='2':
            coverage_final_dict['unMotoristAuto'] = '12'
        elif coverage_final_dict['unMotoristAuto'] =='7':
            coverage_final_dict['unMotoristAuto'] = '17'

    
    if coverage_dict['hired_borrowed_checkbox'] == "YES":
        if coverage_dict['liability_type'] =='CSL':
            
            if coverage_dict['liability_amount1'] != "":
                coverage_final_dict['cslSingleLimit'] = coverage_dict['liability_amount1']
            elif coverage_dict['liability_amount2'] != "":
                coverage_final_dict['cslSingleLimit'] = coverage_dict['liability_amount2']          
            elif coverage_dict['liability_amount3'] != "":
                coverage_final_dict['cslSingleLimit'] = coverage_dict['liability_amount3']

            coverage_final_dict['cslSingleAuto'] = '18'

        elif coverage_dict['liability_type'] =='BI_EAPER':

            coverage_final_dict['cslBodyPerPerson'] = coverage_dict['liability_amount1']
            coverage_final_dict['cslBodyPerAccident'] = coverage_dict['liability_amount2']
            coverage_final_dict['cslProperty'] = coverage_dict['liability_amount3']
            coverage_final_dict['cslSplitAuto'] = "18"

    if coverage_dict['non_owned_checkbox'] == "YES":
        if coverage_dict['liability_type'] =='CSL':
            
            if coverage_dict['liability_amount1'] != "":
                coverage_final_dict['nonCslSingleLimit'] = coverage_dict['liability_amount1']
            elif coverage_dict['liability_amount2'] != "":
                coverage_final_dict['nonCslSingleLimit'] = coverage_dict['liability_amount2']           
            elif coverage_dict['liability_amount3'] != "":
                coverage_final_dict['nonCslSingleLimit'] = coverage_dict['liability_amount3']

            coverage_final_dict['nonCslSingleAuto'] = '18'

        elif coverage_dict['liability_type'] =='BI_EAPER':                  

            coverage_final_dict['nonCslBodyPerPerson'] = coverage_dict['liability_amount1']
            coverage_final_dict['nonCslBodyPerAccident'] = coverage_dict['liability_amount2']
            coverage_final_dict['nonCslProperty'] = coverage_dict['liability_amount3']
            coverage_final_dict['nonCslSplitAuto'] = "18"

    if coverage_dict['deductible_checkbox'] != "":
        coverage_final_dict['deductable'] = "YES"
        coverage_final_dict['deductableAutoEntry'] = '17'
    deduct_list = []

    if coverage_dict['deductible_amount1'] != "":
        deduct_list.append(coverage_dict['deductible_amount1'])
        #coverage_final_dict['underinsuredMotoristSingleLimit'] = coverage_dict['deductible_amount1']
        
    if coverage_dict['deductible_amount2'] != "":
        #coverage_final_dict['underinsuredMotoristSingleLimit'] = coverage_dict['deductible_amount2']  
        deduct_list.append(coverage_dict['deductible_amount2'])  
                
    if coverage_dict['deductible_amount3'] != "":
        #coverage_final_dict['underinsuredMotoristSingleLimit'] = coverage_dict['deductible_amount3']
        deduct_list.append(coverage_dict['deductible_amount3'])  
        
    if coverage_dict['deductible_checkbox'] != "":
        coverage_final_dict['deductableAmount'] = " , ".join(deduct_list)


    if csl_amount>=1000000 or biea_amount>=1000000:
        coverage_final_dict['underinsuredMotoristPremium'] = "250"
        coverage_final_dict['uninsuredMotoristPremium'] = "250"

    return coverage_final_dict

# print(main_coverage(r"/data/INADEV/final_txt/T & J UNLIMITED TRANSPORTATION INC ACCORD.txt"))

