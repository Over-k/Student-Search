import json

with open('students.json', 'r') as f:
    data = json.load(f)

def unique(results):
    updated = {}
    for item in results:
        name = item['cin']
        if name in updated:
            updated[name]['cne'] = item['cne'] if len(updated[name]['cne'])  < len(item['cne']) else updated[name]['cne']
            updated[name]['nationality'] = item['nationality'] if len(updated[name]['nationality']) < len(item['nationality']) else updated[name]['nationality']
            updated[name]['fullname'] = item['fullname'] if len(updated[name]['fullname']) < len(item['fullname']) else updated[name]['fullname']
            updated[name]['date_birthday'] = item['date_birthday'] if len(updated[name]['date_birthday']) < len(item['date_birthday']) else updated[name]['date_birthday']
            updated[name]['gender'] = item['gender'] if len(updated[name]['gender']) < len(item['gender']) else updated[name]['gender']
            updated[name]['address'] = item['address'] if len(updated[name]['address']) < len(item['address']) else updated[name]['address']
            updated[name]['code_postal'] = item['code_postal'] if len(updated[name]['code_postal']) < len(item['code_postal']) else updated[name]['code_postal']
            updated[name]['phone'] = item['phone'] if len(updated[name]['phone']) < len(item['phone']) else updated[name]['phone']
            updated[name]['email'] = item['email'] if len(updated[name]['email']) < len(item['email']) else updated[name]['email']
            updated[name]['father'] = item['father'] if len(updated[name]['father']) < len(item['father']) else updated[name]['father']
            updated[name]['mather'] = item['mather'] if len(updated[name]['mather'])  < len(item['mather']) else updated[name]['mather']
        else:
            updated[name] = {'cin': item['cin'],'cne': item['cne'], 'nationality': item['nationality'], 'fullname': item['fullname'], 'date_birthday': item['date_birthday'], 'gender': item['gender'], 'address': item['address'], 'code_postal': item['code_postal'], 'phone': item['phone'], 'email': item['email'], 'father': item['father'], 'mather': item['mather']}
    updated = [v for k, v in updated.items()]
    return updated
  
def search(key, value,max):
    results = []
    for item in data:
        if key in item and item[key].lower() == value.lower():
            results.append(item)
        if max < len(results):
            break
    return unique(results)
