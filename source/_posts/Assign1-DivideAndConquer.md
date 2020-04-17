---
title: Assign1-DivideAndConquer
mathjax: true
date: 2018-01-25 10:55:10
tags:
categories:
	- Algorithms
thumbnail: 0-0.png
password: 180055
abstract: This blog is encrypted.
message: You must enter the password to read.
---

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign1-DivideAndConquer/20190113151538.png)



![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign1-DivideAndConquer/20190114110221.png)

### 1 Divide and Conquer 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign1-DivideAndConquer/20190114110304.png)

每次将数组二分，取A，B数组的中位数比较，若$A[m_A]<B[m_B]$则$0-m_A$必属于两数组排序后的前n个数中，我们反证，若$A[m_A]<B[m_B]$,A中$0-m_A$不完全属于前n个数，则第n个数小于$A[m_A]$，又因为$A[m_A]<B[m_B]$，则B中比$A[m_A]$小的数小于$\frac{n}{2}$，则A，B中小于$A[m_A]$的个数必小于$n$，因此假设不成立。每次递归过程会使问题规模减小$\frac{1}{2}$，直到$A[m_A]=B[m_B]$，或者问题规模减少到1，因此，经过有限次递归，可以得到问题解。

由$(b)$中的子问题图可知，问题规模每次递归减少$\frac{1}{2}$，因此共有$\log n$层，每层的时间复杂度为$O(n)$，因此，总时间复杂度为$O(\log n)$。

### 2 Divide and Conquer 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign1-DivideAndConquer/20190114110329.png)

随机选取pivot，将比pivot小的数移动至pivot左边，比pivot大的数移动到pivot右边，比较$|S_+|$与k-1的大小，若小于k-1，则说明$k^{th}$ largest数在$S_-$中，若大于k-1，则说明$k^{th}$\ largest数在$S_+$中，若等于，则$k^{th}$\ largest是pivot。

$T(n)\ =\ T(\frac{n}{2})+C$，总时间复杂度与QuickSelect一样为$O(n)$。

### 3 Divide and Conquer 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign1-DivideAndConquer/20190114110352.png)

对于完全二叉树T，总存在全局最小值，也即存在局部最小值，local minimum一定存在。对于lable of node v，若其小于左右child，则其为local minimum，若lable of node v只大于左（右）child，就递归左（右）子树，而右（左）child大于父节点，因此其不用递归。

完全二叉树共有$\log n$层，每层时间复杂度为$O(n)$，因此$T(n)\ =\ O(\log n)$。

### 4 Divide and Conquer 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign1-DivideAndConquer/20190114110415.png)

不断四分，最后到3*3的格子，localmin要么是边界最小值，要么是中心点，必有localmin。

时间复杂度$T(n)=T(\frac{n}{4})+O(n)$ ，为$O(n)$ 。

### 5 Divide and Conquer 

![](https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/https://cdn.jsdelivr.net/gh/xmzzyo/Blog@master/source/_posts/Assign1-DivideAndConquer/20190114110428.png)

选取多边形一条随机边$v_1,v_2$，以及点$p_n$，可以构成一个三角形和两个多变形，其中一个多边形边数为i，另个一个是v-i+1，且$p_n$在满足两个多变形至少为三角形的前提下，可以任取。因此i的取值为2到n-1，解为卡特兰数，满足$f(n)=f(2)\times f(n-1)+f(3)\times f(n-2)+f(4)\times f(n-3)+\cdots+f(n-1)\times f(2)$。

保存计算结果，$T(n)\ =\ O(n^2)$。

### 6 Divide and Conquer 

若a[i] <= 3*a[j] : i++
否则a[i] > 3*a[j]: 说明此时满足条件，cnt += n ­ i , 最后j++ 

当大于三倍右边时，计左半部分i右边的个数。

$O(n\log n)$

### 7 Divide and Conquer 

```java
package SortAndCount;
import java.io.*;
public class SAC {

    private int len = 100000;
    private int[] data = new int[len];
    private long Qc = 0;

    public SAC(int len, int[] data) {
        this.len = len;
        this.data = data;
    }

    public static SAC newInstance(int len, int[] data){
        return new SAC(len, data);
    }

    public int[] getData() {
        return data;
    }

    // MergeAndSort 计算逆序数
    public long SortAndCount(int l, int r) {
        if (l == r)
            return 0;
        int m = (l + r) / 2;
        long lrc = SortAndCount(l, m);
        long rrc = SortAndCount(m + 1, r);
        long rc = MergeAndCount(l, m, r);
        return lrc + rrc + rc;
    }

    public long MergeAndCount(int l, int m, int r) {
        long rc = 0;
        int i = l, j = m + 1, p = 0;
        int[] res = new int[len];
        while (i <= m && j <= r) {
            if (data[i] > data[j]) {
                res[p] = data[j];
                j++;
                p++;
                // 左边 data[i] 比 data[j] 大，则 data[i] 左边的数比 data[j] 都大，
                // 共有 m-i-1 个逆序对
                rc += m - i + 1;
            } else {
                res[p] = data[i];
                i++;
                p++;
            }
        }
        // 没有遍历完的左右数组，继续赋值给 res 数组
        while (i <= m) {
            res[p] = data[i];
            p++;
            i++;
        }
        while (j <= r) {
            res[p] = data[j];
            p++;
            j++;
        }
        p = 0;
        // 将 Merge 后的数组 res 赋给 data
        for (int k = l; k <= r; k++, p++) {
            data[k] = res[p];
        }
        return rc;
    }

    // 快排计算逆序数
    public long QSortAndCount(int l, int r) {
        if (l < r) {
            int pivot = Partition(l, r);
            QSortAndCount(l, pivot - 1);
            QSortAndCount(pivot + 1, r);
        }
        return Qc;
    }

    private int Partition(int l, int r) {
        int i = l + 1, p = l;
        int[] left = new int[len];
        while (i <= r) {
            if (data[i] < data[l]) {
                left[p] = data[i];
                //当找到小于pivot的数时，移到左边，
                //由该数以及在其左侧比它大的数构成逆序数对，
                //左侧比它大的数共有 i-p 个，即总数减去比 pivot 小的数，就是比其大的数，
                //因为从左到右依次与 pivot 比较，因此该数与已经移到左侧的数依然保持相对有序，移动不会减少
                //逆序数对移到左侧后，即消除了 i-p 个逆序对，可以继续比较、移动
                Qc += i - p;
                p++;
            }
            i++;
        }
        left[p] = data[l];
        int pivot = p;
        p++;
        // 将比 pivot 大的数继续放在 left 数组右边
        for (i = l + 1; i <= r; i++) {
            if (data[i] >= data[l]) {
                left[p] = data[i];
                p++;
            }
        }
        for (i = l; i <= r; i++) {
            data[i] = left[i];
        }
        return pivot;
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("Q8.txt"));
        String line = null;
        int i = 0;
        int[] data = new int[100000];
        while ((line = br.readLine()) != null) {
            data[i++] = Integer.parseInt(line.trim());
        }
        long rc;
        long start, end;
        start = System.currentTimeMillis();
        rc = SAC.newInstance(i,data).SortAndCount(0, i-1);
        end = System.currentTimeMillis();
        System.out.println(rc);
        System.out.println("MergeSortAndCount cost time: "+(end-start)+"ms");
        /*start = System.currentTimeMillis();
        rc = SAC.newInstance(i, data).QSortAndCount(0, i - 1);
        end = System.currentTimeMillis();
        System.out.println(rc);
        System.out.println("QuickSortAndCount cost time: "+(end-start)+"ms");*/
        /*data = sac.getData();
        for (int k = 0; k < i; k++) {
            System.out.println(data[k]);
        }*/
    }
}
```

### 8 Divide and Conquer 

```java
package Strassen;
public class Strassen {

	// 将矩阵根据起始点 (x,y) 和长度 len ，分成四个子矩阵
    public static int[][] divideMatrix(int src[][], int x, int y, int len) {
        int[][] sub = new int[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                sub[i][j] = src[i + x][j + y];
            }
        }
        return sub;
    }

    // 矩阵合并
    public static int[][] mergeMatrix(int[][] c11, int[][] c12, int[][] c21, int[][] c22) {
        int mlen = c11.length;
        int len = mlen * 2;
        int[][] c = new int[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (i < mlen && j < mlen)
                    c[i][j] = c11[i][j];
                else if (i < mlen && j >= mlen)
                    c[i][j] = c12[i][j - mlen];
                else if (i >= mlen && j < mlen)
                    c[i][j] = c21[i - mlen][j];
                else if (i >= mlen && j >= mlen)
                    c[i][j] = c22[i - mlen][j - mlen];
            }
        }
        return c;
    }

    // 两个矩阵相加
    public static int[][] matrixAdd(int A[][], int B[][]) {
        int len = A.length;
        int[][] C = new int[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                C[i][j] = A[i][j] + B[i][j];
            }
        }
        return C;
    }

	// 两个矩阵相减
    public static int[][] matrixSub(int A[][], int B[][]) {
        int len = A.length;
        int[][] C = new int[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                C[i][j] = A[i][j] - B[i][j];
            }
        }
        return C;
    }


    // Strassen 算法
    public static int[][] strassenMatrixMultiply(int A[][], int B[][]) {
        int len = A.length;
        int mLen = len / 2;
        int C[][] = new int[len][len];
        if (len == 1) {
            C[0][0] = A[0][0] * B[0][0];
            return C;
        }
        int[][] A11, A12, A21, A22, B11, B12, B21, B22;
        A11 = divideMatrix(A, 0, 0, mLen);
        A12 = divideMatrix(A, 0, mLen, mLen);
        A21 = divideMatrix(A, mLen, 0, mLen);
        A22 = divideMatrix(A, mLen, mLen, mLen);
        B11 = divideMatrix(B, 0, 0, mLen);
        B12 = divideMatrix(B, 0, mLen, mLen);
        B21 = divideMatrix(B, mLen, 0, mLen);
        B22 = divideMatrix(B, mLen, mLen, mLen);

        int[][] tmp1, tmp2, tmp3, tmp4, tmp5, tmp6, tmp7, tmp8, tmp9, tmp10;

        tmp1 = matrixSub(B12, B22);
        tmp2 = matrixAdd(A11, A12);
        tmp3 = matrixAdd(A21, A22);
        tmp4 = matrixSub(B21, B11);
        tmp5 = matrixAdd(A11, A22);
        tmp6 = matrixAdd(B11, B22);
        tmp7 = matrixSub(A12, A22);
        tmp8 = matrixAdd(B21, B22);
        tmp9 = matrixSub(A11, A21);
        tmp10 = matrixAdd(B11, B12);

        int[][] P1 = strassenMatrixMultiply(A11, tmp1),
                P2 = strassenMatrixMultiply(tmp2, B22),
                P3 = strassenMatrixMultiply(tmp3, B11),
                P4 = strassenMatrixMultiply(A22, tmp4),
                P5 = strassenMatrixMultiply(tmp5, tmp6),
                P6 = strassenMatrixMultiply(tmp7, tmp8),
                P7 = strassenMatrixMultiply(tmp9, tmp10);

        int[][] tmp;
        int[][] C11, C12, C21, C22;

        tmp = matrixAdd(P4, P5);
        tmp = matrixAdd(tmp, P6);
        C11 = matrixSub(tmp, P2);
        C12 = matrixAdd(P1, P2);
        C21 = matrixAdd(P3, P4);
        tmp = matrixAdd(P1, P5);
        tmp = matrixSub(tmp, P3);
        C22 = matrixSub(tmp, P7);

        C = mergeMatrix(C11, C12, C21, C22);

        return C;
    }

    // GradeSchool 算法
    public static int[][] gradeSchool(int[][] A, int[][] B) {
        int len = A.length;
        int[][] C = new int[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                int sum = 0;
                for (int k = 0; k < len; k++) {
                    sum += A[i][k] * B[k][j];
                }
                C[i][j] = sum;
            }
        }
        return C;
    }

    public static void printMatrix(int[][] m) {
        for (int i = 0; i < m.length; i++) {
            for (int e : m[i]) {
                System.out.print(e + " ");
            }
            System.out.print("\n");
        }
    }

    public static void main(String args[]) {
        int[][] A = new int[][]{
                {1, 2, 3, 4, 5, 6, 7, 8},
                {1, 2, 3, 4, 5, 6, 7, 8},
                {1, 2, 3, 4, 5, 6, 7, 8},
                {1, 2, 3, 4, 5, 6, 7, 8},
                {5, 6, 7, 8, 1, 2, 3, 4},
                {5, 6, 7, 8, 1, 2, 3, 4},
                {5, 6, 7, 8, 1, 2, 3, 4},
                {5, 6, 7, 8, 1, 2, 3, 4}
        };

        int[][] B = new int[][]{
                {5, 6, 7, 8, 1, 2, 3, 4},
                {5, 6, 7, 8, 1, 2, 3, 4},
                {5, 6, 7, 8, 1, 2, 3, 4},
                {5, 6, 7, 8, 1, 2, 3, 4},
                {1, 2, 3, 4, 5, 6, 7, 8},
                {1, 2, 3, 4, 5, 6, 7, 8},
                {1, 2, 3, 4, 5, 6, 7, 8},
                {1, 2, 3, 4, 5, 6, 7, 8}
        };

        int[][] C;

        long start = System.nanoTime();
        C = Strassen.strassenMatrixMultiply(A, B);
        long end = System.nanoTime();
        Strassen.printMatrix(C);
        System.out.println("Strassen cost time: " + (end - start) / 1000 + "ms");
        System.out.println();
        start = System.nanoTime();
        C = Strassen.gradeSchool(A, B);
        end = System.nanoTime();
        Strassen.printMatrix(C);
        System.out.println("GradeSchool cost time: " + (end - start) / 1000 + "ms");
    }


}
```



