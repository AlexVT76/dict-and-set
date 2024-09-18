my_dict={'Denis': 1030,'Pavel': 1031}
print('Dict:',my_dict)
print('Existing value:',my_dict.get('Denis'))
print('Not existing value:',my_dict.get('Anna'))
my_dict.update({'Max': 1032,'Alina': 1000})
a=my_dict.pop('Denis')
print('Deleted value:', a)
print('Modified dictionary:',my_dict)
my_set={'people',2024,3.14,'dog',2024,3.14}
print('Set:',my_set)
my_set.add('cat')
my_set.add(27.5)
my_set.discard(2024)
print('Modified set:',my_set)

