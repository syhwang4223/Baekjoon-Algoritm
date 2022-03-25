## 문제

어드벤처 게임을 하던 중, 1부터 n까지의 번호가 붙은 방을 지나가야 하는 마법의 미로를 마주쳤다. 각 방 안에는 번호가 붙은 문이 있을 수 있고, 각 문은 해당하는 번호의 방으로 통한다. 방 안에는 레프리콘이나 트롤이 있을 수도 있다.

레프리콘이 있는 방에 들어가면 레프리콘은 모험가의 소지금이 일정 양 이하로 떨어지지 않게 채워준다. 레프리콘은 모험가의 소지금이 일정량 미만일 때에는 그만한 양이 되도록 금화를 채워주고, 소지금이 일정량 이상일 때에는 그대로 둔다. 트롤이 있는 방에 들어가려면 일정량의 통행료를 지불해야 한다. 이는 맨 처음에 모험가가 1번 방에서 시작하려 할 때에도 마찬가지이다.

모험가는 소지금이 0인 상태에서 출발한다. 과연 모험가는 1번 방에서 출발해서 n번 방에 도착할 수 있을까?

## 입력

입력은 여러 개의 미로로 주어진다. 각 미로의 첫 줄에는 미로의 방 수를 나타내는 정수 n(1 ≤ n ≤ 1000)이 주어진다. 다음 n 줄에는 각 방의 정보가 주어진다. 각 방의 정보는 방의 내용물을 나타내는 알파벳 하나(E: 빈 방, L: 레프리콘, T: 트롤)와 그 방의 레프리콘이나 트롤이 정해놓은 금액(빈 방일 경우 0이고, 금액은 500보다 작거나 같은 자연수), 그리고 그 방에서 다른 방으로 갈 수 있는 문의 번호들로 이루어진다. 각 줄은 0으로 끝난다. 미로의 방 수가 0개인 입력이 들어오면 입력을 종료한다.

## 출력

출력은 각 미로마다 한 줄씩으로 이루어진다. 각 줄에는 1번 방에서 n번 방까지 갈 수 있는지를 "Yes" 또는 "No"로 출력한다.

## 예제 입력 1 복사

```
3
E 0 2 0
L 10 3 0
T 15 1 2 0
4
E 0 2 3 0
L 201 2 3 0
L 10 4 0
T 15 2 3 1 0
0
```

## 예제 출력 1 복사

```
No
Yes
```

## 출처

[ICPC](https://www.acmicpc.net/category/1) > [Regionals](https://www.acmicpc.net/category/7) > [South Pacific](https://www.acmicpc.net/category/92) > [South Pacific Region](https://www.acmicpc.net/category/104) > [New Zealand Programming Contest](https://www.acmicpc.net/category/93) > [NZPC 2005](https://www.acmicpc.net/category/detail/1143) O번

- 빠진 조건을 찾은 사람: [qwer9412](https://www.acmicpc.net/user/qwer9412)
- 문제를 번역한 사람: [thebarbershop](https://www.acmicpc.net/user/thebarbershop)