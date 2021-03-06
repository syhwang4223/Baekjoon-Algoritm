## 문제

N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

## 입력

첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

## 출력

첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

## 예제 입력 1 복사

```
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
```

## 예제 출력 1 복사

```
4
```

## 출처

- 데이터를 추가한 사람: [djm03178](https://www.acmicpc.net/user/djm03178), [qf9ar8nv](https://www.acmicpc.net/user/qf9ar8nv), [sait2000](https://www.acmicpc.net/user/sait2000)
- 시간 제한을 수정한 사람: [djm03178](https://www.acmicpc.net/user/djm03178)
- 문제의 오타를 찾은 사람: [HowlingOfSouL](https://www.acmicpc.net/user/HowlingOfSouL), [ibjsw](https://www.acmicpc.net/user/ibjsw)
- 잘못된 데이터를 찾은 사람: [hsnks100](https://www.acmicpc.net/user/hsnks100)
- 빠진 조건을 찾은 사람: [jh05013](https://www.acmicpc.net/user/jh05013), [luke0201](https://www.acmicpc.net/user/luke0201), [toysmars](https://www.acmicpc.net/user/toysmars)

## 알고리즘 분류

- [그래프 이론](https://www.acmicpc.net/problem/tag/7)
- [다익스트라](https://www.acmicpc.net/problem/tag/22)