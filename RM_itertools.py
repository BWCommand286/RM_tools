
import pandas as pd

def dict_values_to_list(d):
    
    for key in d.keys():
        
        if not isinstance(d[key], list):
            d[key] = [d[key]]
        
    return d

def dict_merge(dict_list):
    
    result_dict = {}
    
    for idx, d in enumerate(dict_list):
        d = dict_values_to_list(d)
        intersection, rest_d, rest_result = compare_lists(d.keys(), result_dict.keys())
                
        for key in intersection:
            result_dict[key] = result_dict[key]+d[key]
            
        for key in rest_d:
            result_dict[key] = ['']*idx+d[key]
            
        for key in rest_result:
            result_dict[key] = result_dict[key]+['']
            
    return pd.DataFrame(result_dict)

#Alternative zu dict_merge aus pandas:
def dict_merge_pd(dict_list):
    
    # Creating the first Dataframe using dictionary
    df1 = pd.DataFrame({"a":[1, 2, 3, 4],
                        "b":[5, 6, 7, 8]})
      
    # Creating the Second Dataframe using dictionary
    df2 = pd.DataFrame({"a":[1, 2, 3],
                        "b":[5, 6, 7], 
                        "c":[1, 5, 4]})
      
    # for appending df2 at the end of df1
    df1.append(df2, ignore_index = True)

def compare_lists(list_1, list_2):
    
    intersection = []
    rest_1 = []
    rest_2 = []
    
    for item in list_1:
        
        if item in list_2:
            intersection.append(item)
        else:
            rest_1.append(item)
            
    for item in list_2:
        
        if item not in list_1:
            rest_2.append(item)
            
    return intersection, rest_1, rest_2

def dict_walker(dictionary):
    
    dict_list = []
   
    n = 0
    n_list = []
    n_list.append(n)
    
    StopLoop = False
    
    f = open('dict_walker.txt','w')
    
    while StopLoop == False:
        
        if n == 0:
            
            dict_list.append(dictionary)
            dictionary = dict_list[-1]
            
            if isinstance(dictionary, dict):
                keys = sorted(list(dictionary.keys()))
            elif isinstance(dictionary, list):
                keys = range(0,len(dictionary))
                        
        
        if len(keys) > n:
            
            text = (len(n_list)-1)*'\t'+str(keys[n])+'\n'
            print(text)
            f.write(text)
            x = dictionary[keys[n]]
            if isinstance(x, dict):
                
                dictionary = x
                n = 0
                n_list.append(n)
            elif isinstance(x, list):
                dictionary = x
                n = 0
                n_list.append(n)   
                
            else:
                
                n = n_list[-1]
                n += 1
                n_list[-1] = n
            
        else:
            
            if len(dict_list[:-1]) > 0:
                
                n_list = n_list[:-1]
                n = n_list[-1]
                n += 1
                n_list[-1] = n
                
                dict_list = dict_list[:-1]
                dictionary = dict_list[-1]

                if isinstance(dictionary, dict):
                    keys = sorted(list(dictionary.keys()))
                elif isinstance(dictionary, list):
                    keys = range(0,len(dictionary))
                    
            else:
                
                StopLoop = True
                break
    f.close()
    print('\n')

"""Funktion zum Inspizieren von Objekten"""
def object_tester(sample):
    result = []
    
    for attr in dir(sample):
        if callable(getattr(sample, attr)):
            try:
                result.append(getattr(sample, attr)())
            except Exception as e:
                print(e)
                result.append(getattr(sample, attr))
        else:
            result.append(getattr(sample, attr))
    return result

def tab_print(*args):
    
    print_str = ''
    
    for arg in args:
        print_str += str(arg)+'\t'
        
    print(print_str)
