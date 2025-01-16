### **ROW_NUMBER() OVER (PARTITION BY hcp_id ORDER BY contact_date DESC)**

#### 설명:
- `ROW_NUMBER()`는 특정 기준에 따라 행에 고유 번호를 부여합니다.
- `PARTITION BY`는 데이터를 그룹화합니다. 각 그룹 내에서 행 번호를 지정합니다.
- `ORDER BY`는 각 그룹 내에서 어떤 순서로 번호를 지정할지 결정합니다.

#### 예제:
```sql
SELECT 
    hcp_id,
    contact_date,
    ROW_NUMBER() OVER (PARTITION BY hcp_id ORDER BY contact_date DESC) AS row_num
FROM 
    hcp_contacts;
```

#### 입력 데이터:
| hcp_id | contact_date |
|--------|--------------|
| a1의원 | 2024-03-12   |
| a1의원 | 2024-03-13   |
| b3의원 | 2024-03-15   |
| c2병원 | 2024-03-16   |

#### 결과:
| hcp_id | contact_date | row_num |
|--------|--------------|---------|
| a1의원 | 2024-03-13   | 1       |
| a1의원 | 2024-03-12   | 2       |
| b3의원 | 2024-03-15   | 1       |
| c2병원 | 2024-03-16   | 1       |

- **요점:** 같은 병원(`hcp_id`)에 속한 데이터끼리 묶이고, `contact_date DESC` 기준으로 최신 날짜가 첫 번째(1번) 번호를 받습니다.