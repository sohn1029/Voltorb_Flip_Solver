# Voltorb Flip Solver

<img src = "https://user-images.githubusercontent.com/31722713/187972328-51f43f3a-996d-4a7b-a9b0-eea2917e891b.jpg" width=30% height=30%>

## 해결 방법

When we try to solve this problem with brute force algorithm, we need to check the number of cases of 4^25.  

So I decided to figure out the number of cases that could come out of each horizontal line and see if they were valid when combined.  

This method can reduce the number of cases up to 90^5.  

However, this is not a small number ,too.  

Therefore, I suggested a backtracking technique to solve this problem.  

For this technique, we can make two pruning rules.  

First, when adding each line, make sure that the number of zeros does not exceed presented in the bottom rule.  

Second, reduce the number of cases through what is already known.  

In this way, you can solve the problem quickly, but the answer is not unique, so let's think of it as a good tip.  

우리가 만약 이 문제를 브루트포스로 해결하려고 하면 4^25의 경우의 수를 확인하여야 한다.  

그래서 각 가로줄에서 나올 수 있는 경우의 수를 미리 만들어 놓고, 이것을 결합하였을 때 유효한지 확인하도록 하였다.

이 방법으로 우리는 확인하여야 할 경우의 수를 최대 90^5까지 줄일 수 있다.

하지만 이것 또한 작은 숫자는 아니다.

그래서 나는 이 문제를 풀기 위해 백트래킹을 사용하였다.

이 방법을 위해서 우리는 두 가지 가지치기 규칙을 만들 수 있다.

첫번째로, 각 줄을 추가하면서 0의 개수가 '아래 규칙'에 제시된 0의 개수를 초과하지 않는지 확인한다.

둘째로, 이미 알게된 부분을 통해 경우의 수를 줄이는 것이다.  

이러한 방법으로, 우리는 문제를 빠르게 해결할 수 있지만, 답이 유일하지 않으므로 좋은 팁 정도로만 생각하자.  

## 사용 방법

In the code, right_rule is a list of rules on the right side of the board in order from top to bottom.  

And, bottom_rule is the left-to-right list of rules at the bottom of the board.  

A board is a list containing information that is already known.(-1 is unknown)

When the code is executed after writing the information, various correct answers are output first.  

Then, the location with the number and bomb is printed out.

코드에서, right_rule은 보드의 오른쪽에 있는 규칙을 위에서 아래로 나열한 것이다.  

그리고, bottom_rule은 보드의 아래쪽에 있는 규칙을 오른쪽에서 왼쪽으로 나열한 것이다.

board에는 이미 알고 있는 정보를 넣을 수 있다.(-1은 모르는 곳)

정보가 입력된 후 코드를 실행시키면 다양한 정답들이 먼저 출력된다.

그리고, 숫자와 폭탄이 있을 곳을 출력한다.

## 필요한 라이브러리  

- Numpy
