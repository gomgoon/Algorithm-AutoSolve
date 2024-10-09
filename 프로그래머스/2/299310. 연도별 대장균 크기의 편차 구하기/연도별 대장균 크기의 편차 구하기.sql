SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, 
    D3.SIZE - D1.SIZE_OF_COLONY AS YEAR_DEV, 
    ID
FROM ECOLI_DATA D1
JOIN (
    SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR, MAX(SIZE_OF_COLONY) AS SIZE
    FROM ECOLI_DATA D2 
    GROUP BY YEAR
) D3
ON YEAR(D1.DIFFERENTIATION_DATE) = D3.YEAR
ORDER BY YEAR ASC, YEAR_DEV ASC;