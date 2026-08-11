# Octave Publishing Report

## Publisher: `Ben Manning`

---

## File 1: `functionTest.m` (Function)

### 1. Code

```matlab
function out1 = functionTest(a,b,c)

    x = -5:c;
    y = a.*(x.^2) + b;

    out1 = 2.5*a + 8*b + 4*c;

    plot(x,y);

end
```

### 2. Execution Details

Arguments Used:

```matlab
40,50,30
```

### 3. Console Output

```text

```

### 4. Function Return Values

* **Output #1:** `620`

### 5. Generated Plot(s)

1 plot found

#### Plot 1:
![Plot 1 Reference](functionTest_plot_1.png)


---

## File 2: `scriptTest.m` (Script)

### 1. Code

```matlab
x = 1:10;
y = x.^2;

disp("Hello There")

plot(x,y,'*',"color",'r')
```

### 2. Execution Details

### 3. Console Output

```text
Hello There
```

### 4. Generated Plot(s)

1 plot found

#### Plot 1:
![Plot 1 Reference](scriptTest_plot_1.png)


---

