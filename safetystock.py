# 창고의 재고 데이터가 dictionary 형태로 주어집니다. 각 제품의 현재 재고량과 최소 재고량(safety stock)이 있을 때,
# 재주문이 필요한 제품들의 목록과 주문 필요 수량을 반환하는 함수를 작성하세요.
# 1. 현재 재고가 safety stock 미만인 제품을 찾습니다.
# 2. 각 제품별로 max_capacity까지 채우기 위해 필요한 주문량을 계산합니다.
# 3. 결과는 dictionary 형태로 반환합니다: {제품코드: 주문필요수량}
inventory = {
    'A001': {'current': 150, 'safety_stock': 100, 'max_capacity': 300},
    'B002': {'current': 80, 'safety_stock': 100, 'max_capacity': 250},
    'C003': {'current': 200, 'safety_stock': 150, 'max_capacity': 350},
    'D004': {'current': 90, 'safety_stock': 100, 'max_capacity': 200}
}
print('# keys')
print(inventory.keys())
print('# values')
print(inventory.values())
print('# items')
print(inventory.items())
print('# A001 keys')
print(inventory['A001'].keys())
print('# A001 values')
print(inventory['A001'].values())
print(inventory['A001']['current'])
print(inventory['A001']['current'])
# dictionary는 key, value
# 제품 목록은 key, 주문 필요 수량은 value
# inventory.items() -> [('A001', {'current': 150, 'safety_stock': 100, 'max_capacity': 300}), ('B002', {'current': 80, 'safety_stock': 100, 'max_capacity': 250}), ('C003', {'current': 200, 'safety_stock': 150, 'max_capacity': 350}), ('D004', {'current': 90, 'safety_stock': 100, 'max_capacity': 200})]

# if inventory.current < inventory.safety_stock:
#        order = inventory.max_capacity - inventory.current
def reorder(inventory):
    product_stock = {} # key: product, value: order stock
    for product, stock in inventory.items():
        # e.g. product = 'A001', stock = {'current': 150, 'safety_stock': 100, 'max_capacity': 300}
        if stock['current'] < stock['safety_stock']:
            ### dictionary[key] -> value
            product_stock[product] = stock['max_capacity'] - stock['current']
    return product_stock

print(reorder(inventory))