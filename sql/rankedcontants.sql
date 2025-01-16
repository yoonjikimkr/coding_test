-- Task: Remove duplicates in hcp_contacts table based on hcp_id and contact_date, keeping only the latest entry.

WITH RankedContacts AS (
    SELECT 
        hcp_id,
        contact_date,
        ROW_NUMBER() OVER (PARTITION BY hcp_id ORDER BY contact_date DESC) AS row_num
    FROM 
        hcp_contacts
)
DELETE FROM hcp_contacts
WHERE 
    hcp_id IN (
        SELECT hcp_id FROM RankedContacts WHERE row_num > 1
    );

-- CTE means Common Table Expression.
-- It is a temporary result set that is defined within the execution scope of
-- a single SELECT, INSERT, UPDATE, DELETE, or CREATE VIEW statement.
-- CTE: RankedContacts
-- ROW_NUMBER() assigns a rank to rows based on contact_date in descending order.
-- Deletes rows where row_num > 1, retaining only the latest contact per HCP.