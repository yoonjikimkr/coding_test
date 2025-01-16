#### **A. 누적 합계 계산**
**Task:** 월별 누적 판매 금액을 계산하세요.

```sql
SELECT 
    EXTRACT(MONTH FROM sales_date) AS month,
    SUM(sales_amount) AS monthly_sales,
    SUM(SUM(sales_amount)) OVER (ORDER BY EXTRACT(MONTH FROM sales_date)) AS cumulative_sales
FROM 
    sales_data
WHERE 
    EXTRACT(YEAR FROM sales_date) = 2024
GROUP BY 
    EXTRACT(MONTH FROM sales_date)
ORDER BY 
    month;
```

**결과:**
| month | monthly_sales | cumulative_sales |
|-------|---------------|------------------|
| 1     | 250           | 250              |
| 2     | 450           | 700              |

---

#### **B. RANK()를 활용한 상위 판매 제품 선정**
**Task:** 월별 가장 많이 판매된 제품의 순위를 매겨보세요.

```sql
SELECT 
    product_id,
    EXTRACT(MONTH FROM sales_date) AS month,
    SUM(sales_amount) AS total_sales,
    RANK() OVER (PARTITION BY EXTRACT(MONTH FROM sales_date) ORDER BY SUM(sales_amount) DESC) AS rank
FROM 
    sales_data
WHERE 
    EXTRACT(YEAR FROM sales_date) = 2024
GROUP BY 
    product_id, EXTRACT(MONTH FROM sales_date)
ORDER BY 
    month, rank;
```

**결과:**
| product_id | month | total_sales | rank |
|------------|-------|-------------|------|
| P001       | 1     | 200         | 1    |
| P002       | 1     | 100         | 2    |
| P003       | 2     | 300         | 1    |

---

#### **C. 중복 데이터 제거**
**Task:** `sales_data` 테이블에서 중복된 행을 제거하세요.

```sql
WITH RankedSales AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY product_id, sales_date ORDER BY sales_id) AS row_num
    FROM 
        sales_data
)
DELETE FROM sales_data
WHERE 
    sales_id IN (
        SELECT sales_id FROM RankedSales WHERE row_num > 1
    );
```

**해설:**
- 중복된 `product_id`와 `sales_date`가 있는 행에 대해 `ROW_NUMBER()`로 각 행에 번호를 매깁니다.
- `row_num > 1`인 행만 삭제하여 중복을 제거합니다.

---

### 연습이 필요한 추가 과제:
1. **Top N 제품의 연간 매출 추출.**
2. **특정 병원에서 처방된 약품의 매출 기여도 분석.**
3. **신규 제품이 전체 매출에서 차지하는 비율 계산.**
4. **특정 기간 동안 판매량이 가장 낮은 영업사원 찾기.**