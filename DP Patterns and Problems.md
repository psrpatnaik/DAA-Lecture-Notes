
Compiled from LeetCode
======================

(P.S.R.Patnaik)
===============

Index:
======

[Compiled from LeetCode](#h.l6w1zuafes19)

[(P.S.R.Patnaik)](#h.besaxjku6dxq)

[Index:](#h.j5rvf5z0uf9a)

[DP Problem Patterns](#h.7p3moqnk2y6f)

[Minimum (Maximum) Path to Reach a Target](#h.hm0b5vt7px7u)

[Statement](#h.v4vhycol5k29)

[Approach](#h.el8q18k6830u)

[Similar Problems](#h.vprobsqk5td)

[Distinct Ways](#h.j19h98pem311)

[Statement](#h.wsrqxyxt9q2v)

[Approach](#h.kjqxdreybsgy)

[Similar Problems](#h.exvrkw1o08o8)

[Merging Intervals](#h.xroin455hlhm)

[Statement](#h.a5y2y343bbtw)

[Approach](#h.douaiqvunozw)

[Similar Problems](#h.5mbjyie3sna8)

[DP on Strings](#h.5rzngwk6vmzf)

[Statement](#h.od07c3lstaj)

[Approach](#h.aj9j1ee8f4ky)

[Decision Making](#h.xcpusp3qpira)

[Statement](#h.mkndmkhbv0ql)

[Approach](#h.qxjylk58cfn1)

[From good to great. How to approach most DP problems.](#h.vgkeknkvvefj)

* * *

DP Problem Patterns
===================

* * *

1.  Minimum (Maximum) Path to Reach a Target
2.  Distinct Ways
3.  Merging Intervals
4.  DP on Strings
5.  Decision Making

Minimum (Maximum) Path to Reach a Target
========================================

* * *

Generate problem statement for this pattern

### Statement

Given a target find minimum (maximum) cost / path / sum to reach the target.

### Approach

Choose minimum (maximum) path among all possible paths before the current state, then add value for the current state.

routes\[i\] = min(routes\[i\-1\], routes\[i\-2\], ... , routes\[i-k\]) + cost\[i\]

Generate optimal solutions for all values in the target and return the value for the target.

for (int i = 1; i <= target; ++i) {

 for (int j = 0; j < ways.size(); ++j) {

 if (ways\[j\] <= i) {

 dp\[i\] = min(dp\[i\], dp\[i - ways\[j\]\]) + cost / path / sum;

 }

 }

}

return dp\[target\]

### Similar Problems

[746\. Min Cost Climbing Stairs](https://www.google.com/url?q=https://leetcode.com/problems/min-cost-climbing-stairs/&sa=D&source=editors&ust=1627719362113000&usg=AOvVaw1yefBs6_Nc1OaqB1bzvkUY) Easy

for (int i = 2; i <= n; ++i) {

 dp\[i\] = min(dp\[i\-1\], dp\[i\-2\]) + (i == n ? 0 : cost\[i\]);

}

return dp\[n\]

[64\. Minimum Path Sum](https://www.google.com/url?q=https://leetcode.com/problems/minimum-path-sum/&sa=D&source=editors&ust=1627719362114000&usg=AOvVaw0X8oQrmbyhWdFTk9TvbxKM) Medium

for (int i = 1; i < n; ++i) {

 for (int j = 1; j < m; ++j) {

 grid\[i\]\[j\] = min(grid\[i\-1\]\[j\], grid\[i\]\[j\-1\]) + grid\[i\]\[j\];

 }

}

return grid\[n\-1\]\[m\-1\]

[322\. Coin Change](https://www.google.com/url?q=https://leetcode.com/problems/coin-change/&sa=D&source=editors&ust=1627719362115000&usg=AOvVaw2VQ9Br425JYMSkOehEbpJR) Medium

for (int j = 1; j <= amount; ++j) {

 for (int i = 0; i < coins.size(); ++i) {

 if (coins\[i\] <= j) {

 dp\[j\] = min(dp\[j\], dp\[j - coins\[i\]\] + 1);

 }

 }

}

[931\. Minimum Falling Path Sum](https://www.google.com/url?q=https://leetcode.com/problems/minimum-falling-path-sum/&sa=D&source=editors&ust=1627719362116000&usg=AOvVaw1tLBNf-wmUKzlpVLEwwSs1) Medium

[983\. Minimum Cost For Tickets](https://www.google.com/url?q=https://leetcode.com/problems/minimum-cost-for-tickets/&sa=D&source=editors&ust=1627719362117000&usg=AOvVaw2BO9WKPkN5a_-xwwSbj_ZS) Medium

[650\. 2 Keys Keyboard](https://www.google.com/url?q=https://leetcode.com/problems/2-keys-keyboard/&sa=D&source=editors&ust=1627719362117000&usg=AOvVaw0ms8823baKVmXYNqhO8xWs) Medium

[279\. Perfect Squares](https://www.google.com/url?q=https://leetcode.com/problems/perfect-squares/&sa=D&source=editors&ust=1627719362118000&usg=AOvVaw1rlzHCjHmrlsL7SnVFdgsX) Medium

[1049\. Last Stone Weight II](https://www.google.com/url?q=https://leetcode.com/problems/last-stone-weight-ii/&sa=D&source=editors&ust=1627719362118000&usg=AOvVaw3caU1heh8Jwv5xygt0i-4H) Medium

[120\. Triangle](https://www.google.com/url?q=https://leetcode.com/problems/triangle/&sa=D&source=editors&ust=1627719362118000&usg=AOvVaw3TyrF6WT0ONp9x0FlsWrlz) Medium

[474\. Ones and Zeroes](https://www.google.com/url?q=https://leetcode.com/problems/ones-and-zeroes/&sa=D&source=editors&ust=1627719362119000&usg=AOvVaw3mBUgiNG4Y5mtXO7z2B6ZW) Medium

[221\. Maximal Square](https://www.google.com/url?q=https://leetcode.com/problems/maximal-square/&sa=D&source=editors&ust=1627719362119000&usg=AOvVaw11Z-CJOAPOqZU8mQCaYBNS) Medium

[322\. Coin Change](https://www.google.com/url?q=https://leetcode.com/problems/coin-change/&sa=D&source=editors&ust=1627719362120000&usg=AOvVaw0t4FB9SABuVGZdZTIUSghV) Medium

[1240\. Tiling a Rectangle with the Fewest Squares](https://www.google.com/url?q=https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/&sa=D&source=editors&ust=1627719362120000&usg=AOvVaw3Jim1_gDVYCIUDz8Vx757l) Hard

[174\. Dungeon Game](https://www.google.com/url?q=https://leetcode.com/problems/dungeon-game/&sa=D&source=editors&ust=1627719362120000&usg=AOvVaw0vpAcIRZ6QAghTw9G8-lrh) Hard

[871\. Minimum Number of Refueling Stops](https://www.google.com/url?q=https://leetcode.com/problems/minimum-number-of-refueling-stops/&sa=D&source=editors&ust=1627719362121000&usg=AOvVaw31CUyN7lxlW89v_HAtwc3k) Hard

Distinct Ways
=============

* * *

Generate problem statement for this pattern

### Statement

Given a target find a number of distinct ways to reach the target.

### Approach

Sum all possible ways to reach the current state.

routes\[i\] = routes\[i\-1\] + routes\[i\-2\], ... , + routes\[i-k\]

Generate sum for all values in the target and return the value for the target.

for (int i = 1; i <= target; ++i) {

 for (int j = 0; j < ways.size(); ++j) {

 if (ways\[j\] <= i) {

 dp\[i\] += dp\[i - ways\[j\]\];

 }

 }

}

return dp\[target\]

### Similar Problems

[70\. Climbing Stairs](https://www.google.com/url?q=https://leetcode.com/problems/climbing-stairs/&sa=D&source=editors&ust=1627719362123000&usg=AOvVaw0Ra53HCQBCsqTtdxxcVzIz) easy

for (int stair = 2; stair <= n; ++stair) {

 for (int step = 1; step <= 2; ++step) {

 dp\[stair\] += dp\[stair-step\]; 

 }

}

[62\. Unique Paths](https://www.google.com/url?q=https://leetcode.com/problems/unique-paths/&sa=D&source=editors&ust=1627719362124000&usg=AOvVaw26FcTghgDTfQ5VsTzrMe-L) Medium

for (int i = 1; i < m; ++i) {

 for (int j = 1; j < n; ++j) {

 dp\[i\]\[j\] = dp\[i\]\[j\-1\] + dp\[i\-1\]\[j\];

 }

}

[1155\. Number of Dice Rolls With Target Sum](https://www.google.com/url?q=https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/&sa=D&source=editors&ust=1627719362125000&usg=AOvVaw0UBzVxelCwGvrH4o_O4Nl5) Medium

for (int rep = 1; rep <= d; ++rep) {

 vector<int\> new\_ways(target+1);

 for (int already = 0; already <= target; ++already) {

 for (int pipe = 1; pipe <= f; ++pipe) {

 if (already - pipe >= 0) {

 new\_ways\[already\] += ways\[already - pipe\];

 new\_ways\[already\] %= mod;

 }

 }

 }

 ways = new\_ways;

}

Note

Some questions point out the number of repetitions, in that case, add one more loop to simulate every repetition.

[688\. Knight Probability in Chessboard](https://www.google.com/url?q=https://leetcode.com/problems/knight-probability-in-chessboard/&sa=D&source=editors&ust=1627719362127000&usg=AOvVaw0Yr7L5MfwWUbVNx0Nvl_ve) Medium

[494\. Target Sum](https://www.google.com/url?q=https://leetcode.com/problems/target-sum/&sa=D&source=editors&ust=1627719362128000&usg=AOvVaw1VuwqbJ09XHkqT3a2VkQ7O) Medium

[377\. Combination Sum IV](https://www.google.com/url?q=https://leetcode.com/problems/combination-sum-iv/&sa=D&source=editors&ust=1627719362128000&usg=AOvVaw0BaoQs8uxRT7XE_eWTpESf) Medium

[935\. Knight Dialer](https://www.google.com/url?q=https://leetcode.com/problems/knight-dialer/&sa=D&source=editors&ust=1627719362128000&usg=AOvVaw26tbif0jD4vvlFKqDIfoQy) Medium

[1223\. Dice Roll Simulation](https://www.google.com/url?q=https://leetcode.com/problems/dice-roll-simulation/&sa=D&source=editors&ust=1627719362129000&usg=AOvVaw1TvH4sC0AXP3dca8ehvaN8) Medium

[416\. Partition Equal Subset Sum](https://www.google.com/url?q=https://leetcode.com/problems/partition-equal-subset-sum/&sa=D&source=editors&ust=1627719362129000&usg=AOvVaw0tQG58XMbGocZL8eFFMsOK) Medium

[808\. Soup Servings](https://www.google.com/url?q=https://leetcode.com/problems/soup-servings/&sa=D&source=editors&ust=1627719362130000&usg=AOvVaw3yYNrFayDGPdtgNqcuCR4P) Medium

[790\. Domino and Tromino Tiling](https://www.google.com/url?q=https://leetcode.com/problems/domino-and-tromino-tiling/&sa=D&source=editors&ust=1627719362130000&usg=AOvVaw1I8HRmlurQlNhdYu7slWZo) Medium

[801\. Minimum Swaps To Make Sequences Increasing](https://www.google.com/url?q=https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/&sa=D&source=editors&ust=1627719362131000&usg=AOvVaw0C-7mkmcoYMk8BsN4nJN6q)

[673\. Number of Longest Increasing Subsequence](https://www.google.com/url?q=https://leetcode.com/problems/number-of-longest-increasing-subsequence/&sa=D&source=editors&ust=1627719362131000&usg=AOvVaw2hOH3StKGyE7zOPgg1xNWR) Medium

[63\. Unique Paths II](https://www.google.com/url?q=https://leetcode.com/problems/unique-paths-ii/&sa=D&source=editors&ust=1627719362132000&usg=AOvVaw3sEWZ7zLzDx4zFsvZDF5Dy) Medium

[576\. Out of Boundary Paths](https://www.google.com/url?q=https://leetcode.com/problems/out-of-boundary-paths/&sa=D&source=editors&ust=1627719362132000&usg=AOvVaw072xJV3fAJYfyZ8nT7T1L-) Medium

[1269\. Number of Ways to Stay in the Same Place After Some Steps](https://www.google.com/url?q=https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/&sa=D&source=editors&ust=1627719362132000&usg=AOvVaw1eG8OrByhE0G0iwajjlVoL) Hard

[1220\. Count Vowels Permutation](https://www.google.com/url?q=https://leetcode.com/problems/count-vowels-permutation/&sa=D&source=editors&ust=1627719362133000&usg=AOvVaw3NOOmNwRxlTvc1JUDrs_Ra) Hard

Merging Intervals
=================

* * *

Generate problem statement for this pattern

### Statement

Given a set of numbers, find an optimal solution for a problem considering the current number and the best you can get from the left and right sides.

### Approach

Find all optimal solutions for every interval and return the best possible answer.

// from i to j

dp\[i\]\[j\] = dp\[i\]\[k\] + result\[k\] + dp\[k+1\]\[j\]

Get the best from the left and right sides and add a solution for the current position.

for(int l = 1; l<n; l++) {

 for(int i = 0; i<n-l; i++) {

 int j = i+l;

 for(int k = i; k<j; k++) {

 dp\[i\]\[j\] = max(dp\[i\]\[j\], dp\[i\]\[k\] + result\[k\] + dp\[k+1\]\[j\]);

 }

 }

}

return dp\[0\]\[n\-1\]

### Similar Problems

[1130\. Minimum Cost Tree From Leaf Values](https://www.google.com/url?q=https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/&sa=D&source=editors&ust=1627719362136000&usg=AOvVaw0TrXw-946KmgfIHeDIN8bZ) Medium

for (int l = 1; l < n; ++l) {

 for (int i = 0; i < n - l; ++i) {

 int j = i + l;

 dp\[i\]\[j\] = INT\_MAX;

 for (int k = i; k < j; ++k) {

 dp\[i\]\[j\] = min(dp\[i\]\[j\], dp\[i\]\[k\] + dp\[k+1\]\[j\] + maxs\[i\]\[k\] \* maxs\[k+1\]\[j\]);

 }

 }

}

[96\. Unique Binary Search Trees](https://www.google.com/url?q=https://leetcode.com/problems/unique-binary-search-trees/&sa=D&source=editors&ust=1627719362137000&usg=AOvVaw16GwtOQaERZB3VRO51IR0C) Medium

[1039\. Minimum Score Triangulation of Polygon](https://www.google.com/url?q=https://leetcode.com/problems/minimum-score-triangulation-of-polygon/&sa=D&source=editors&ust=1627719362138000&usg=AOvVaw3WZRJWOZnYIWIUmQ7OPdoz) Medium

[546\. Remove Boxes](https://www.google.com/url?q=https://leetcode.com/problems/remove-boxes/&sa=D&source=editors&ust=1627719362138000&usg=AOvVaw3_pSFJf8bLuHJxevBmffBl) Medium

[1000\. Minimum Cost to Merge Stones](https://www.google.com/url?q=https://leetcode.com/problems/minimum-cost-to-merge-stones/&sa=D&source=editors&ust=1627719362138000&usg=AOvVaw1mOT8B7yVgmbSMFFXxynEw) Medium

[312\. Burst Balloons](https://www.google.com/url?q=https://leetcode.com/problems/burst-balloons/&sa=D&source=editors&ust=1627719362139000&usg=AOvVaw1g3_DYmuBGqyXOIDuVbj6J) Hard

[375\. Guess Number Higher or Lower II](https://www.google.com/url?q=https://leetcode.com/problems/guess-number-higher-or-lower-ii/&sa=D&source=editors&ust=1627719362139000&usg=AOvVaw3NUXi-aT5zMY9HhxvgTLiV) Medium

DP on Strings
=============

* * *

General problem statement for this pattern can vary but most of the time you are given two strings where lengths of those strings are not big

### Statement

Given two strings s1 and s2, return some result.

### Approach

Most of the problems on this pattern requires a solution that can be accepted in O(n^2) complexity.

// i - indexing string s1

// j - indexing string s2

for (int i = 1; i <= n; ++i) {

 for (int j = 1; j <= m; ++j) {

 if (s1\[i\-1\] == s2\[j\-1\]) {

 dp\[i\]\[j\] = /\*code\*/;

 } else {

 dp\[i\]\[j\] = /\*code\*/;

 }

 }

}

If you are given one string s the approach may little vary

for (int l = 1; l < n; ++l) {

 for (int i = 0; i < n-l; ++i) {

 int j = i + l;

 if (s\[i\] == s\[j\]) {

 dp\[i\]\[j\] = /\*code\*/;

 } else {

 dp\[i\]\[j\] = /\*code\*/;

 }

 }

}

[1143\. Longest Common Subsequence](https://www.google.com/url?q=https://leetcode.com/problems/longest-common-subsequence/&sa=D&source=editors&ust=1627719362144000&usg=AOvVaw1kaLlFC6_Q4jlzkg5Ke5Be) Medium

for (int i = 1; i <= n; ++i) {

 for (int j = 1; j <= m; ++j) {

 if (text1\[i\-1\] == text2\[j\-1\]) {

 dp\[i\]\[j\] = dp\[i\-1\]\[j\-1\] + 1;

 } else {

 dp\[i\]\[j\] = max(dp\[i\-1\]\[j\], dp\[i\]\[j\-1\]);

 }

 }

}

[647\. Palindromic Substrings](https://www.google.com/url?q=https://leetcode.com/problems/palindromic-substrings/&sa=D&source=editors&ust=1627719362146000&usg=AOvVaw2f0Kx59Q0-TfJJW6mdLfHc) Medium

for (int l = 1; l < n; ++l) {

 for (int i = 0; i < n-l; ++i) {

 int j = i + l;

 if (s\[i\] == s\[j\] && dp\[i+1\]\[j\-1\] == j-i\-1) {

 dp\[i\]\[j\] = dp\[i+1\]\[j\-1\] + 2;

 } else {

 dp\[i\]\[j\] = 0;

 }

 }

}

[516\. Longest Palindromic Subsequence](https://www.google.com/url?q=https://leetcode.com/problems/longest-palindromic-subsequence/&sa=D&source=editors&ust=1627719362148000&usg=AOvVaw138w4sAA-7YUoDwsWEmoH9) Medium

[1092\. Shortest Common Supersequence](https://www.google.com/url?q=https://leetcode.com/problems/shortest-common-supersequence/&sa=D&source=editors&ust=1627719362148000&usg=AOvVaw0klJ-qBRSDsbD8mDmsMyLP) Medium

[72\. Edit Distance](https://www.google.com/url?q=https://leetcode.com/problems/edit-distance/&sa=D&source=editors&ust=1627719362148000&usg=AOvVaw3yBICvg3xH076djsV8kx3e) Hard

[115\. Distinct Subsequences](https://www.google.com/url?q=https://leetcode.com/problems/distinct-subsequences/&sa=D&source=editors&ust=1627719362149000&usg=AOvVaw37qAVPYMy3qQ2Yve78hDeE) Hard

[712\. Minimum ASCII Delete Sum for Two Strings](https://www.google.com/url?q=https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/&sa=D&source=editors&ust=1627719362149000&usg=AOvVaw09eEbENQNh3T_BL3kfmhNU) Medium

[5\. Longest Palindromic Substring](https://www.google.com/url?q=https://leetcode.com/problems/longest-palindromic-substring/&sa=D&source=editors&ust=1627719362149000&usg=AOvVaw1M0zqktGnErALJejEXv2Tm) Medium

Decision Making
===============

* * *

The general problem statement for this pattern is forgiven situation decide whether to use or not to use the current state. So, the problem requires you to make a decision at a current state.

### Statement

Given a set of values find an answer with an option to choose or ignore the current value.

### Approach

If you decide to choose the current value use the previous result where the value was ignored; vice-versa, if you decide to ignore the current value use previous result where value was used.

// i - indexing a set of values

// j - options to ignore j values

for (int i = 1; i < n; ++i) {

 for (int j = 1; j <= k; ++j) {

 dp\[i\]\[j\] = max({dp\[i\]\[j\], dp\[i\-1\]\[j\] + arr\[i\], dp\[i\-1\]\[j\-1\]});

 dp\[i\]\[j\-1\] = max({dp\[i\]\[j\-1\], dp\[i\-1\]\[j\-1\] + arr\[i\], arr\[i\]});

 }

}

[198\. House Robber](https://www.google.com/url?q=https://leetcode.com/problems/house-robber/&sa=D&source=editors&ust=1627719362152000&usg=AOvVaw0yLfW9E4IPz4sUYiwZ734A) Easy

for (int i = 1; i < n; ++i) {

 dp\[i\]\[1\] = max(dp\[i\-1\]\[0\] + nums\[i\], dp\[i\-1\]\[1\]);

 dp\[i\]\[0\] = dp\[i\-1\]\[1\];

}

[121\. Best Time to Buy and Sell Stock](https://www.google.com/url?q=https://leetcode.com/problems/best-time-to-buy-and-sell-stock/&sa=D&source=editors&ust=1627719362154000&usg=AOvVaw2j_nuUKI0v-k0NUyIobP_Z) Easy

[714\. Best Time to Buy and Sell Stock with Transaction Fee](https://www.google.com/url?q=https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/&sa=D&source=editors&ust=1627719362154000&usg=AOvVaw3EZYc0iZhVbjXXz4d7EX_1) Medium

[309\. Best Time to Buy and Sell Stock with Cooldown](https://www.google.com/url?q=https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/&sa=D&source=editors&ust=1627719362155000&usg=AOvVaw15t3GGgOzxQxytimGw3Tio) Medium

[123\. Best Time to Buy and Sell Stock III](https://www.google.com/url?q=https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/&sa=D&source=editors&ust=1627719362155000&usg=AOvVaw1Z4NKAHRsZwd0CkqHY-C1t) Hard

[188\. Best Time to Buy and Sell Stock IV](https://www.google.com/url?q=https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/&sa=D&source=editors&ust=1627719362155000&usg=AOvVaw2pHOG6SairNX569epTgcnp) Hard

* * *

From good to great. How to approach most DP problems.
=====================================================

There is some frustration when people publish their perfect fine-grained algorithms without sharing any information abut how they were derived. This is an attempt to change the situation. There is not much more explanation but it's rather an example of higher level improvements. Converting a solution to the next step shouldn't be as hard as attempting to come up with perfect algorithm at first attempt.

This particular problem and most of others can be approached using the following sequence:

1.  Find recursive relation
2.  Recursive (top-down)
3.  Recursive + memo (top-down)
4.  Iterative + memo (bottom-up)
5.  Iterative + N variables (bottom-up)

Step 1. Figure out recursive relation.

A robber has 2 options: a) rob current house i; b) don't rob current house.

If an option "a" is selected it means she can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.

If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.

So it boils down to calculating what is more profitable:

*   robbery of current house + loot from houses before the previous
*   loot from the previous house robbery and any loot captured before that

rob(i) = Math.max( rob(i - 2) + currentHouseValue, rob(i - 1) )

Step 2. Recursive (top-down)

Converting the recurrent relation from Step 1 shound't be very hard.

public int rob(int\[\] nums) {

 return rob(nums, nums.length - 1);

}

private int rob(int\[\] nums, int i) {

 if (i < 0) {

 return 0;

 }

 return Math.max(rob(nums, i - 2) + nums\[i\], rob(nums, i - 1));

}

This algorithm will process the same i multiple times and it needs improvement. Time complexity: \[to fill\]

Step 3. Recursive + memo (top-down).

int\[\] memo;

public int rob(int\[\] nums) {

 memo = new int\[nums.length + 1\];

 Arrays.fill(memo, \-1);

 return rob(nums, nums.length - 1);

}

private int rob(int\[\] nums, int i) {

 if (i < 0) {

 return 0;

 }

 if (memo\[i\] >= 0) {

 return memo\[i\];

 }

 int result = Math.max(rob(nums, i - 2) + nums\[i\], rob(nums, i - 1));

 memo\[i\] = result;

 return result;

}

Much better, this should run in O(n) time. Space complexity is O(n) as well, because of the recursion stack, let's try to get rid of it.

Step 4. Iterative + memo (bottom-up)

public int rob(int\[\] nums) {

 if (nums.length == 0) return 0;

 int\[\] memo = new int\[nums.length + 1\];

 memo\[0\] = 0;

 memo\[1\] = nums\[0\];

 for (int i = 1; i < nums.length; i++) {

 int val = nums\[i\];

 memo\[i+1\] = Math.max(memo\[i\], memo\[i\-1\] + val);

 }

 return memo\[nums.length\];

}

Step 5. Iterative + 2 variables (bottom-up)

We can notice that in the previous step we use only memo\[i\] and memo\[i-1\], so going just 2 steps back. We can hold them in 2 variables instead. This optimization is met in Fibonacci sequence creation and some other problems \[to paste links\].

/\* the order is: prev2, prev1, num  \*/

public int rob(int\[\] nums) {

 if (nums.length == 0) return 0;

 int prev1 = 0;

 int prev2 = 0;

 for (int num : nums) {

 int tmp = prev1;

 prev1 = Math.max(prev2 + num, prev1);

 prev2 = tmp;

 }

 return prev1;

}

Quite commonly, dp tables are built such that dp\[m\]\[n\] is the ultimate solution. However, there are also a number of DP problems where a variable is updated when building the dp table and the variables contain the final answer(e.g., Problem 647).

Last note: keeps practicing! I think I would review those problems for several rounds in the coming weeks, just to keep myself comfortable with DP. When practicing, try to solve with recursive, memoization, tabulation, and even optimize the space when possible.
