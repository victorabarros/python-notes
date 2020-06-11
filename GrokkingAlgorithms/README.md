# Grokking Algorithms

> https://www.oreilly.com/library/view/grokking-algorithms-an/9781617292231/

## 6 Breadth-first Search



## 8 Greedy

**Problem**: Suppose you’re starting a radio show. You want to reach listeners in all 50 states. You have to decide what stations to play on to reach all those listeners. It costs money to be on each station, so you’re trying to minimize the number of stations you play on. You have a list of stations:
a human scale: [Font]( https://www.prowesscorp.com/computer-latency-at-a-human-scale/)

|Station|Avaiable in  |
|-------|-----------  |
|kone   |in id, nv, ut|
|ktwo   |in wa, id, mt|
|ktree  |in or, nv    |

Every possible subset, is called the power set, are 2^n possible. (Fórmula do subconjunto de algebra)

**Greedy algorithms**:

- Step 1: Pick the station that covers the most states that haven’t been covered yet. It’s OK if the station covers some states that have been covered already.
- Step 2: Repeat until all the states are covered.

> Greedy is called an approximation algorithm. When calculating the exact solution will take too much time, an approximation algorithm will work.
