import re
import json

def names_function(content):
    # with open(file_path, 'r') as file:
    #     content = file.readlines()
    # print(content)
    #data = content.split('\n')
    #data = data[:20]
    result = []
    ver_list=[]
    main_list=[]
    # agency_pattern = r'PROPOSED EFF DATE'
    #agency_pattern = r"DRIVER\s+(.*?)\s*\*\s*\s+MAR"
    agency_pattern = r"DRIVER\s+(.*?)\s+MAR"
    agency_pattern2 = r"Driver\s+(.*?)\s+DATE"
    end_pattern = r"* MARITAL STATUS / CIVIL UNION (if applicable)"
    names_pattern = r'[A-Za-z.-]+$'

    for k,l in enumerate(content):
        #print("@@@@@@@@@@@@@@@@@@@'",l)
        match = re.search(agency_pattern,l)   #NOTE                         ##ridewithcar
        match2 = re.search(agency_pattern2,l)   #NOTE
        if match or match2:
            #print("Y")
            #print(l)
            if match:
                span = match.span()
            else:
                span = match2.span()
            #print(l[span[1]-10:])
            for i in range(1,80):
                
                next_line = content[k+i]
                #print(next_line)
                if '* MARITAL STATUS / CIVIL UNION (if applicable)' in next_line or 'ACORD 163' in next_line or 'GENERAL INFORMATION' in next_line or 'VEHICLE DESCRIPTION' in next_line:
                    #print("!")
                    break
                if 'SEX' not in next_line and 'Driver' not in next_line and '#' not in next_line and 'CITY' not in next_line and 'DATE' not in next_line and 'Street' not in next_line:
                    #print("!!")
                    #print(next_line)
                    if len(next_line)!=0:
                    #print(next_line)
                        ver_data = next_line[span[0]:span[1]+10]
                        ver_list = ver_data.split()
                        #print(ver_list)
                        if 'M' in ver_list:
                            male_index = ver_list.index('M')
                            ver_list = ver_list[:male_index]
                            if 'F' in ver_list:
                                ver_list.remove('F')
                            ver_data = " ".join(ver_list)
                        elif 'F' in ver_list:
                            female_index = ver_list.index('F')
                            ver_list = ver_list[:female_index]
                            ver_data = " ".join(ver_list)
                        elif 'U' in ver_list:
                            u_index = ver_list.index('U')
                            ver_list = ver_list[:u_index]
                            ver_data = " ".join(ver_list)
                       
                           
                        ver_data = ver_data.strip()
                        ver_data = re.sub(r'\s+', ' ', ver_data)
                        #print(ver_data)
                        match_date = re.search(names_pattern,ver_data)
                        if match_date and len(ver_data.strip())!=0:
                            #print("!!!!!!!!!!!!!")
                            #print(ver_data)
                            match_ver = match_date.span()
                            #print(match_ver)

                            ver_data = ver_data.strip()
                            ver_data = ver_data[:match_ver[1]]
                            ver_data =  re.sub(r'\d', '', ver_data)
                            main_list.append(ver_data.strip())

                            #print("%%%%%%%%%",ver_list)
                        else:
                            continue
            #s1 = ' '.join(ver_list)
            #s1 = s1.split()[0]
            # print(main_list)
            return main_list

        # Check if the string is not blank


    return ""


def license_function(content):
    # with open(file_path, 'r') as file:
    #     content = file.readlines()
    #data = content.split('\n')
    #data = data[:20]
    result = []
    ver_list=[]
    main_list=[]
    # agency_pattern = r'PROPOSED EFF DATE'
    #agency_pattern = r"DRIVER\s+(.*?)\s*\*\s*\s+MAR"
    agency_pattern = r"SOCIAL SECURITY NUMBER"
    agency_pattern2 = r"DRIVERS LICENSE NUMBER/"
    #end_pattern = r"* MARITAL STATUS / CIVIL UNION (if applicable)"
    names_pattern = r"^[A-Za-z0-9]+"
    for k,l in enumerate(content):        
        
        match = re.search(agency_pattern,l)   #NOTE                         ##ridewithcar
        match2 = re.search(agency_pattern2,l)   #NOTE
        if match or match2:
            #print("Y")
            #print(l)
            if match:
                span = match.span()
            else:
                span = match2.span()
            #print(l[span[1]-10:])
            for i in range(1,80):
                
                next_line = content[k+i]
                #print(next_line)
                if '* MARITAL STATUS / CIVIL UNION (if applicable)' in next_line or 'ACORD 163' in next_line or 'GENERAL INFORMATION' in next_line or 'VEHICLE DESCRIPTION' in next_line:
                    #print("!")
                    break
                if 'SEX' not in next_line and 'Driver' not in next_line and '#' not in next_line and 'CITY' not in next_line and 'DATE' not in next_line and 'Street' not in next_line and 'LIC' not in next_line and 'SOCIAL' not in next_line:
                    #print("!!")
                    #print(next_line)
                    if len(next_line)!=0:
                    #print(next_line)
                        ver_data = next_line[span[0]-50:span[1]+20]
                        split_ver_data = re.split(r'\s{2,}', ver_data)
                        
                        for q in split_ver_data:
                            q = q.strip()
                            #print("$$$$$",q)
                            if len(q)>=6 and '/' not in q:
                                match_date = re.search(names_pattern,q)
                                if match_date:
                                    
                                    # print("!!!!!!!!!!!!!")
                                    # #print(ver_data)
                                    # match_ver = match_date.span()
                                    # #print(match_ver)

                                    # # ver_data = q.strip()
                                    # ver_data = ver_data[:match_ver[1]]
                                    # ver_data =  re.sub(r'\d', '', ver_data)
                                    q = q.replace('\n','')
                                    main_list.append(q)

                                    #print("%%%%%%%%%",ver_list)
                                else:
                                    continue
            #s1 = ' '.join(ver_list)
            #s1 = s1.split()[0]
            return main_list

        # Check if the string is not blank
    return ""

def state_function(content):
    # with open(file_path, 'r') as file:
    #     content = file.readlines()
    #data = content.split('\n')
    #data = data[:20]
    result = []
    ver_list=[]
    main_list=[]
    # agency_pattern = r'PROPOSED EFF DATE'
    
    #agency_pattern = r"DRIVER\s+(.*?)\s*\*\s*\s+MAR"
    agency_pattern = r"STATE"
    agency_pattern2 = r"STATE LIC"
    #end_pattern = r"* MARITAL STATUS / CIVIL UNION (if applicable)"
    names_pattern = r"\s+[A-Z]{2}\s+"

    for k,l in enumerate(content):        
        
        match = re.search(agency_pattern,l)   #NOTE                         ##ridewithcar
        match2 = re.search(agency_pattern2,l)   #NOTE
        if match or match2:
            #print("Y")
            #print(l)
            if match:
                span = match.span()
            else:
                span = match2.span()
             
            #print(l[span[1]-10:])
            for i in range(1,80):
                
                next_line = content[k+i]
                #print(next_line)
                if '* MARITAL STATUS / CIVIL UNION (if applicable)' in next_line or 'ACORD 163' in next_line or 'GENERAL INFORMATION' in next_line or 'VEHICLE DESCRIPTION' in next_line:
                    #print("!")
                    break
                if 'SEX' not in next_line and 'Driver' not in next_line and '#' not in next_line and 'CITY' not in next_line and 'DATE' not in next_line and 'Street' not in next_line and 'LIC' not in next_line and 'SOCIAL' not in next_line:
                    #print("!!")
                    #print(next_line)
                    if len(next_line)!=0:
                    #print(next_line)
                        ver_data = next_line[span[0]-30:span[1]+20]
                        match_date = re.findall(names_pattern,ver_data)
                        if match_date:
                            main_list.append("".join(match_date).strip())

                        #split_ver_data = re.split(r'\s{2,}', ver_data)
                        
                        # for q in split_ver_data:
                        #     q = q.strip()
                        #     #print("$$$$$",q)
                        #     if len(q)>=6 and '/' not in q:
                        #         match_date = re.search(names_pattern,q)
                        #         if match_date:
                                    
                                    
                        #             q = q.replace('\n','')
                        #             main_list.append(q)

                        #             #print("%%%%%%%%%",ver_list)
                        #         else:
                        #             continue
            #s1 = ' '.join(ver_list)
            #s1 = s1.split()[0]
            return main_list

        # Check if the string is not blank

    return ""


def birth_function(content):
    # with open(file_path, 'r') as file:
    #     content = file.readlines()
    #data = content.split('\n')
    #data = data[:20]
    result = []
    ver_list=[]
    main_list=[]
    # agency_pattern = r'PROPOSED EFF DATE

    #agency_pattern = r"DRIVER\s+(.*?)\s*\*\s*\s+MAR"
    agency_pattern = r"DATE OF BIRTH"
    agency_pattern2 = r"BIRTH"
    #end_pattern = r"* MARITAL STATUS / CIVIL UNION (if applicable)"
    names_pattern = r'\d{2}/\d{2}/\d{2,4}'

    for k,l in enumerate(content):        
        
        match = re.search(agency_pattern,l)   #NOTE                         ##ridewithcar
        match2 = re.search(agency_pattern2,l)   #NOTE
        if match or match2:
            #print("Y")
            #print(l)
            if match:
                span = match.span()
            else:
                span = match2.span()
            #print(l[span[1]-10:])
            for i in range(1,80):
                
                next_line = content[k+i]
                #print(next_line)
                if '* MARITAL STATUS / CIVIL UNION (if applicable)' in next_line or 'ACORD 163' in next_line or 'GENERAL INFORMATION' in next_line or 'VEHICLE DESCRIPTION' in next_line:
                    #print("!")
                    break
                if 'SEX' not in next_line and 'Driver' not in next_line and '#' not in next_line and 'CITY' not in next_line and 'DATE' not in next_line and 'Street' not in next_line and 'LIC' not in next_line and 'SOCIAL' not in next_line:
                    #print("!!")
                    #print(next_line)
                    if len(next_line)!=0:
                    #print(next_line)
                        ver_data = next_line[span[0]-30:span[1]+20]
                        split_ver_data = re.split(r'\s{2,}', ver_data)
                        
                        for q in split_ver_data:
                            q = q.strip()
                            #print("$$$$$",q)
                            if len(q)>=4 and '/' in q:
                                match_date = re.search(names_pattern,q)
                                if match_date:
                                    
                                    # print("!!!!!!!!!!!!!")
                                    # #print(ver_data)
                                    # match_ver = match_date.span()
                                    # #print(match_ver)

                                    # # ver_data = q.strip()
                                    # ver_data = ver_data[:match_ver[1]]
                                    # ver_data =  re.sub(r'\d', '', ver_data)
                                    q = q.replace('\n','')
                                    q = re.sub(r'[a-zA-Z]', '', q)
                                    main_list.append(q.strip())

                                    #print("%%%%%%%%%",ver_list)
                                else:
                                    continue
            #s1 = ' '.join(ver_list)
            #s1 = s1.split()[0]
            return main_list

        # Check if the string is not blank

    return ""

def hire_function(content):
    # with open(file_path, 'r') as file:
    #     content = file.readlines()
    #data = content.split('\n')
    #data = data[:20]
    result = []
    ver_list=[]
    main_list=[]
    # agency_pattern = r'PROPOSED EFF DATE'
    #agency_pattern = r"DRIVER\s+(.*?)\s*\*\s*\s+MAR"
    agency_pattern = r"HIRE"
    agency_pattern2 = r"DATE OF HIRE"
    #hor_pattern = r"Date of Hire:"
    hor_pattern = r"Date of Hire:\s*(\d{1,2}/\d{1,2}/\d{2,4})"
    hor_pattern2 = r"Date of Hire\s*(\d{1,2}/\d{1,2}/\d{2,4})"
    hor_pattern3 = r"Date of Hire;\s*(\d{1,2}/\d{1,2}/\d{2,4})"
    hor_pattern4 = r"Date of hire:\s*(\d{1,2}/\d{1,2}/\d{2,4})"
    #end_pattern = r"* MARITAL STATUS / CIVIL UNION (if applicable)"
    names_pattern = r'\d{1,2}/\d{1,2}/\d{2,4}'

    for k,l in enumerate(content):        
        
        match = re.search(agency_pattern,l)   #NOTE                         ##ridewithcar
        match2 = re.search(agency_pattern2,l)   #NOTE
        match_horiz = re.search(hor_pattern,l) 
        match_horiz2 = re.search(hor_pattern2,l) 
        match_horiz3 = re.search(hor_pattern3,l) 
        match_horiz4 = re.search(hor_pattern4,l) 
        #print(l)
        if match_horiz or match_horiz2 or match_horiz3 or match_horiz4:
            
            for i in range(1,80):
                date_h = []
                next_line = content[k+i-1]
                #print(next_line)
                if '* MARITAL STATUS / CIVIL UNION (if applicable)' in next_line or 'ACORD 163' in next_line or 'GENERAL INFORMATION' in next_line or 'VEHICLE DESCRIPTION' in next_line:
                    #print("!")
                    break
                if 'SEX' not in next_line and 'Driver' not in next_line and '#' not in next_line and 'CITY' not in next_line and 'DATE' not in next_line and 'Street' not in next_line and 'LIC' not in next_line and 'SOCIAL' not in next_line:
                    #print("!!")
                    if match_horiz and '/' in next_line and 'Date of Hire' in next_line:
                        text_span = match_horiz.span()
                        text = next_line[:text_span[1]+10]
                        date_h = re.findall(names_pattern, text)
                        #print(date_h)

                    elif match_horiz2 and '/' in next_line and 'Date of Hire' in next_line:
                        text_span = match_horiz2.span()
                        text = next_line[:text_span[1]+10]
                        #print(text)
                        date_h = re.findall(names_pattern, text)
                    
                    elif match_horiz3 and '/' in next_line and 'Date of Hire' in next_line:
                        text_span = match_horiz3.span()
                        text = next_line[:text_span[1]+10]
                        #print(text)
                        date_h = re.findall(names_pattern, text)

                    elif match_horiz4 and '/' in next_line and 'Date of hire' in next_line:
                        text_span = match_horiz4.span()
                        text = next_line[:text_span[1]+10]
                        #print(text)
                        date_h = re.findall(names_pattern, text)
                        #print(date_h)
                    #print(date_h,"AAAAAAAA")
                    date_h = "".join(date_h)
                    
                    if len(date_h.strip())!=0:
                        
                        main_list.append(date_h.strip())
            #print("@@@@@@@@@@@@@@@@@@",main_list)
            return main_list
                    
        elif match or match2:
            #print("Y")
            #print(l)
            if match:
                span = match.span()
            else:
                span = match2.span()
             
            #print(l[span[1]-10:])
            for i in range(1,40):
                
                next_line = content[k+i]
                #print(next_line)
                if '* MARITAL STATUS / CIVIL UNION (if applicable)' in next_line or 'ACORD 163' in next_line or 'GENERAL INFORMATION' in next_line or 'VEHICLE DESCRIPTION' in next_line:
                    #print("!")
                    break
                if 'SEX' not in next_line and 'Driver' not in next_line and '#' not in next_line and 'CITY' not in next_line and 'DATE' not in next_line and 'Street' not in next_line and 'LIC' not in next_line and 'SOCIAL' not in next_line:
                    #print("!!")
                    #print(next_line)
                    if len(next_line)!=0:
                    #print(next_line)
                        ver_data = next_line[span[0]-30:span[1]+20]
                        split_ver_data = re.split(r'\s{2,}', ver_data)
                        
                        for q in split_ver_data:
                            q = q.strip()
                            #print("$$$$$",q)
                            if len(q)>=4 and '/' in q:
                                match_date = re.search(names_pattern,q)
                                if match_date:
                                    
                                    # print("!!!!!!!!!!!!!")
                                    # #print(ver_data)
                                    # match_ver = match_date.span()
                                    # #print(match_ver)

                                    # # ver_data = q.strip()
                                    # ver_data = ver_data[:match_ver[1]]
                                    # ver_data =  re.sub(r'\d', '', ver_data)
                                    q = q.replace('\n','')
                                    q = re.sub(r'[a-zA-Z]', '', q)
                                    main_list.append(q.strip())

                                    #print("%%%%%%%%%",ver_list)
                                else:
                                    continue
            #s1 = ' '.join(ver_list)
            #s1 = s1.split()[0]
            #print(main_list,"!!!!!")
            if len(main_list)==0:
                continue
            return main_list

        # Check if the string is not blank
    return ""

# Input list of strings
#data = ['My name is Rohan                    No. 4333',' ','Gupta                                                       Date','St Io.']

# # Extract names using the defined function
# file_path = r"/data/INADEV/Extraction/new_txt/QUAD CITIES ACCORD.txt"
# drivers_main_dict = []


def driver_names(drivers_main_dict):
    driver_name_list = names_function(file_path)
    for i in driver_name_list:
        drivers_dict = {
        "driverFirstName":"", #Need to extract
        "driverMiddleName":"", #Need to extract
        "driverLastName":"",#Need to extract
        }
        #print(i)
        if len(i)==1:
            drivers_dict['driverFirstName'] = i        
        elif len(i)==2:
            first_n= i.split()[0]
            last_n= i.split()[1]

            drivers_dict['driverFirstName'] = first_n
            drivers_dict['driverLastName'] = last_n

        elif len(i)>2:
            words = i.split()
            first_n = words[0]
            middle_n = words[1:-1]  
            middle_n = " ".join(middle_n)
            last_n = words[-1]
            drivers_dict['driverFirstName'] = first_n
            drivers_dict['driverLastName'] = last_n
            drivers_dict['driverMiddleName'] = middle_n
        #print(drivers_dict)
        drivers_main_dict.append(drivers_dict)
        driver_details = {"driver_details": drivers_main_dict}
        driver_details_json = json.dumps(driver_details, indent=4)
        #print("sssssssss",drivers_main_dict)
    return driver_details_json


def license_number(drivers_main_dict):
    driver_license_list = license_function(file_path)
    for i in driver_license_list:
        drivers_dict = {
            "licenseNumber":i, #Need to extract
            }
        drivers_main_dict.append(drivers_dict)
        driver_details = {"driver_details": drivers_main_dict}
        driver_details_json = json.dumps(driver_details, indent=4)
        #print("sssssssss",drivers_main_dict)
    return driver_details_json
        
    #print(driver_license_list)
#print(license_number(drivers_main_dict))

def birth_date(drivers_main_dict):
    driver_birth_list = birth_function(file_path)
    for i in driver_birth_list:
        drivers_dict = {
            "driverBirthDate":i, #Need to extract
            
            }
        drivers_main_dict.append(drivers_dict)
        driver_details = {"driver_details": drivers_main_dict}
        driver_details_json = json.dumps(driver_details, indent=4)
        #print("sssssssss",drivers_main_dict)
    return driver_details_json

#print(birth_date(drivers_main_dict))

def hire_date(drivers_main_dict):
    driver_hire_list = hire_function(file_path)
    # print(driver_hire_list)
    for i in driver_hire_list:
        drivers_dict = {
            "driverHireDate":i, #Need to extract
            
            }
        drivers_main_dict.append(drivers_dict)
        driver_details = {"driver_details": drivers_main_dict}
        driver_details_json = json.dumps(driver_details, indent=4)
        #print("sssssssss",drivers_main_dict)
    return driver_details_json

#print(hire_date(drivers_main_dict))


def main_drivers(file_path,main_list):
    

    with open(file_path, 'r') as file:
        content = file.readlines()

    
        #print(content)
    
    table = []
    
    for i, line in enumerate(content):
        if (re.search(r'DRIVER INFORMATION',line,re.IGNORECASE) or re.search(r'DRIVER INFORMATION\s+ACORD 163 attached for additional drivers',line,re.IGNORECASE)) and 'SCHEDULE' not in line: 
            temp = []
            for table_line in content[i:]:
                # print(table_line)
                temp.append(table_line)
                if ('* MARITAL STATUS / CIVIL UNION (if applicable)' in table_line or 'ACORD 163' in table_line or 'GENERAL INFORMATION' in table_line or 'VEHICLE DESCRIPTION' in table_line) and 'ACORD 163 attached for additional drivers' not in table_line:
                    # print(temp)
                    table.append(temp)
                    break
    # print("CCCCCCCC",table)    

    #content = table[0]         
    main_result = []    
    for sub_table in table:
        content = sub_table
              ############ IMPORTANT ################

        #print(content_two)
        try:
            driver_name_list = names_function(content)
        except:
            driver_name_list = []
        try:
            driver_license_list = license_function(content)
        except:
            driver_license_list = []
        try:
            driver_birth_list = birth_function(content)
        except:
            driver_birth_list = []
        try:   
            driver_hire_list = hire_function(content)
        except:
            driver_hire_list = []

        try:
            driver_states_list = state_function(content)

        except:
            driver_states_list = []

        # print("SSSSSTATES",driver_states_list)


            # Your list of lists
        data = [driver_name_list,driver_license_list,driver_birth_list,driver_hire_list,driver_states_list]
        # print("DATTTTTTTTA",data)
        # Read your text file
        
        number_drivers = len(driver_name_list)
        result = []
        flag=0
        names_flag=0
        # Iterate through the sublists
        for sublist in data:
            while(names_flag<1):
        
                # Search for the letter and year
                for i,line in enumerate(content):
                    #print(line)
                    while flag<len(sublist):
                        
                        sub_dict = {'driverFirstName':'','driverMiddleName':'','driverLastName':'','licenseNumber': '','driverBirthDate':'','driverHireDate':'','states':''}

                        if len(sublist[flag])==1:
                            sub_dict['driverFirstName'] = sublist[flag]

                        elif len(sublist[flag])==2:
                            first_n= sublist[flag].split()[0]
                            last_n= sublist[flag].split()[1]

                            sub_dict['driverFirstName'] = first_n
                            sub_dict['driverLastName'] = last_n

                        elif len(sublist[flag])>2:
                            words = sublist[flag].split()
                            first_n = words[0]
                            middle_n = words[1:-1]  
                            middle_n = " ".join(middle_n)
                            last_n = words[-1]
                            sub_dict['driverFirstName'] = first_n
                            sub_dict['driverLastName'] = last_n
                            sub_dict['driverMiddleName'] = middle_n

                        fullname = str(sublist[flag])
                        
                        #print("EEEEEEE",sublist)
                        
                        name = fullname.split()[0]
                        #print(identity,'WWWWWWWWWW')
                        if name in content[i]:
                            

                            if number_drivers==1:                     
                            
                                                            
                                for license in data[1]:
                                    
                                    if str(license) in content[i]:
                                        
                                        sub_dict['licenseNumber'] = str(license)
                                        break
                                    elif str(license) in content[i+1]:
                                        sub_dict['licenseNumber'] = str(license)
                                        break
                                    elif str(license) in content[i+2]:
                                        sub_dict['licenseNumber'] = str(license)
                                        break
                                for birth in data[2]:
                                    
                                    if str(birth) in content[i]:
                                        
                                        sub_dict['driverBirthDate'] = str(birth)
                                        break
                                    elif str(birth) in content[i+1]:
                                        
                                        sub_dict['driverBirthDate'] = str(birth)
                                        break
                                    elif str(birth) in content[i+2]:
                                        sub_dict['driverBirthDate'] = str(birth)
                                        break
                                
                                for hire in data[3]:
                                    
                                    if str(hire) in content[i]:
                                        
                                        sub_dict['driverHireDate'] = str(hire)
                                        break
                                    elif str(hire) in content[i+1]:
                                        sub_dict['driverHireDate'] = str(hire)
                                        break
                                for st in data[4]:
                                    
                                    if str(st) in content[i]:
                                        
                                        sub_dict['states'] = str(st)
                                        break
                                    elif str(st) in content[i+1]:
                                        
                                        sub_dict['states'] = str(st)
                                        break
                                    elif str(st) in content[i+2]:
                                        sub_dict['states'] = str(st)
                                        break
                            elif flag==len(data[0])-1:
                                #print(fullname,"KKKKKKKk")
                                for license in data[1]:
                                    
                                    if str(license) in content[i]:
                                        
                                        sub_dict['licenseNumber'] = str(license)
                                        break
                                    

                                    elif str(license) in content[i+1]:
                                        sub_dict['licenseNumber'] = str(license)
                                        break
                                    elif str(license) in content[i+2]:
                                        sub_dict['licenseNumber'] = str(license)
                                        break
                                for birth in data[2]:
                                    
                                    
                                    if str(birth) in content[i]:
                                        
                                        sub_dict['driverBirthDate'] = str(birth)
                                        break
                                    
                                    elif str(birth) in content[i+1]:
                                        sub_dict['driverBirthDate'] = str(birth)
                                        break
                                    elif str(birth) in content[i+2]:
                                        sub_dict['driverBirthDate'] = str(birth)
                                        break
                                    
                                
                                for hire in data[3]:
                                    
                                    if str(hire) in content[i]:
                                        
                                        sub_dict['driverHireDate'] = str(hire)
                                        break
                                    
                                    elif str(hire) in content[i+1]:
                                        sub_dict['driverHireDate'] = str(hire)
                                        break
                                    elif str(hire) in content[i+2]:
                                        sub_dict['driverHireDate'] = str(hire)
                                        break

                                for st in data[4]:
                                    
                                    if str(st) in content[i]:
                                        
                                        sub_dict['states'] = str(st)
                                        break
                                    
                                    elif str(st) in content[i+1]:
                                        sub_dict['states'] = str(st)
                                        break
                                    elif str(st) in content[i+2]:
                                        sub_dict['states'] = str(st)
                                        break

                            elif number_drivers>1:
                                for license in data[1]:
                                    
                                    if str(license) in content[i]:
                                        
                                        sub_dict['licenseNumber'] = str(license)
                                        break
                                    elif str(license) in content[i+1] and sublist[flag+1] not in content[i+1]:
                                        sub_dict['licenseNumber'] = str(license)
                                        break
                                    elif str(license) in content[i+2] and sublist[flag+1] not in content[i+2]:
                                        sub_dict['licenseNumber'] = str(license)
                                        break

                                    
                                for birth in data[2]:
                                    
                                    
                                    if str(birth) in content[i]:
                                        
                                        sub_dict['driverBirthDate'] = str(birth)
                                        break
                                    elif str(birth) in content[i+1] and sublist[flag+1] not in content[i+1]:
                                        
                                        sub_dict['driverBirthDate'] = str(birth)

                                        break 
                                    elif str(birth) in content[i+2] and sublist[flag+1] not in content[i+2]:
                                        sub_dict['driverBirthDate'] = str(birth)
                                        break
                                    
                                    
                                
                                for hire in data[3]:
                                    
                                    if str(hire) in content[i]:
                                        
                                        sub_dict['driverHireDate'] = str(hire)
                                        break
                                    elif str(hire) in content[i+1] and sublist[flag+1] not in content[i+1]:
                                        sub_dict['driverHireDate'] = str(hire)
                                        break
                                    elif str(hire) in content[i+2] and sublist[flag+1] not in content[i+2]:
                                        #print("GYGYGYGYGYG")
                                        sub_dict['driverHireDate'] = str(hire)
                                        break

                                for st in data[4]:
                                    
                                    if str(st) in content[i]:
                                        
                                        sub_dict['states'] = str(st)
                                        break
                                    elif str(st) in content[i+1] and sublist[flag+1] not in content[i+1]:
                                        sub_dict['states'] = str(st)
                                        break
                                    elif str(st) in content[i+2] and sublist[flag+1] not in content[i+2]:
                                        #print("GYGYGYGYGYG")
                                        sub_dict['states'] = str(st)
                                        break

                            flag+=1

                            result.append(sub_dict)
                            #print(result,"SSSSSS")
                        else:
                            break
                
                names_flag+=1
    
        main_result.append(result)

    return main_result

    #return driver_name_list,driver_license_list

def main_driver_final(file_path):
    main_list=[]
    big_list = main_drivers(file_path,main_list)
    json_list = []

    for sublist in big_list:
        for subdict in sublist:
            json_list.append(subdict)

    # json_output = json.dumps(json_list)
    return json_list

# print(main_driver_final(r"/data/INADEV/final_txt/T & J UNLIMITED TRANSPORTATION INC ACCORD.txt"))







