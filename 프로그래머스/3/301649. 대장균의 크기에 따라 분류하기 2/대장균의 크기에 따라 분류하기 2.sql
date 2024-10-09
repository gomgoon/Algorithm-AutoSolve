SELECT ID, CASE 
WHEN NTILE(4) OVER (ORDER BY SIZE_OF_COLONY ASC) = 1 THEN 'LOW'
WHEN NTILE(4) OVER (ORDER BY SIZE_OF_COLONY ASC) = 2 THEN 'MEDIUM'
WHEN NTILE(4) OVER (ORDER BY SIZE_OF_COLONY ASC) = 3 THEN 'HIGH'
WHEN NTILE(4) OVER (ORDER BY SIZE_OF_COLONY ASC) = 4 THEN 'CRITICAL'
END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID ASC;
