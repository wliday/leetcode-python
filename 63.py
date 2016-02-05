class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		if (not obstacleGrid) or (not obstacleGrid[0]): return 0
		
		m, n = len(obstacleGrid), len(obstacleGrid[0])
		if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1: return 0

		for i in len(m):
			for j in len(n):
				if i == 0 and j == 0:
					obstacleGrid[0][0] = 1
				elif obstacleGrid[i][j] == 1:
					obstacleGrid[i][j] = 0
				elif i == 0:
					obstacleGrid[i][j] = obstacleGrid[i][j - 1] * 1
				elif j == 0:
					obstacleGrid[i][j] = obstacleGrid[i - 1][j] * 1
				else:
					obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

		return obstacleGrid[m - 1][n - 1]

