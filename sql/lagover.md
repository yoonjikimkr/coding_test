### **LAG(SUM(sales_amount)) OVER**

#### 설명:
- `LAG()`는 이전 행의 값을 가져오는 함수입니다.
- `OVER`를 사용해 어떤 기준으로 이전 값을 가져올지 정의합니다.
- `LAG(SUM(sales_amount)) OVER`는 누적 판매 합계를 기준으로 이전 달(혹은 이전 행)의 합계를 가져옵니다.

#### 예제:
```sql
SELECT 
    EXTRACT(MONTH FROM sales_date) AS month,
    SUM(sales_amount) AS total_sales,
    LAG(SUM(sales_amount)) OVER (ORDER BY EXTRACT(MONTH FROM sales_date)) AS previous_sales
FROM 
    sales_data
WHERE 
    EXTRACT(YEAR FROM sales_date) = 2024
GROUP BY 
    EXTRACT(MONTH FROM sales_date)
ORDER BY 
    month;
```

#### 입력 데이터:
| sales_date | sales_amount |
|------------|--------------|
| 2024-01-15 | 100          |
| 2024-01-20 | 150          |
| 2024-02-10 | 200          |
| 2024-02-25 | 250          |

#### 결과:
| month | total_sales | previous_sales |
|-------|-------------|----------------|
| 1     | 250         | NULL           |
| 2     | 450         | 250            |

- **요점:** 2월의 `previous_sales`는 1월의 `total_sales`를 가져옵니다. 이렇게 하면 월간 매출 비교가 가능합니다.