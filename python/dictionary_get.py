d = {'a':1, 'b': 2}
print(d.get('c', 3))
print(d.get('c'))
print(d.get('a'))
print(d.get('a', 3))
# dict.get(key, default=None)
# key가 있으면 key에 대응하는 value를 반환합니다.
# key가 없으면 default를 반환합니다.
# default가 없으면 None을 반환합니다.

print(d.keys()) # dict_keys(['a', 'b']) # view object
print(list(d.keys())) # ['a', 'b'] # list로 변환
print(d.values()) # dict_values([1, 2])
print(d.items()) # dict_items([('a', 1), ('b', 2)])

# d.update([{'a': 3}, {'c': -1}]) XXXX wrong.
# dict.update()는 최대 한 개의 인수만 받을 수 있음.
d = {'a': 1, 'b': 2}
d.update({'a': 3, 'c': -1}) # {'a': 3, 'b': 2, 'c': -1}
d.update(d=4) # {'a': 3, 'b': 2, 'c': -1, 'd': 4}
# 업데이트할 시퀀스(리스트, 튜플 등)는 반드시 (key, value) 형태의 튜플로 이루어져야 함.
# 실무에서는 데이터 병합: 여러 데이터 소스를 통합할 때 사용.
# 설정 값 업데이트: 기본 설정값을 새 값으로 덮어쓰기.

print(d)
print('\npop')
print(d.pop('a', 'na')) # a의 value를 반환하고 삭제
print(d.pop('c', 'na')) # c가 없으면 'na'를 반환
print(d)

# 뷰 객체는 주로 딕셔너리 변경을 실시간으로 감시하거나 순회(iteration)할 때 사용
my_dict = {'a': 1, 'b': 2}
print('Before:', my_dict.keys())  # dict_keys(['a', 'b'])
# 딕셔너리 업데이트
my_dict['c'] = 3
print('After:', my_dict.keys())  # dict_keys(['a', 'b', 'c'])

