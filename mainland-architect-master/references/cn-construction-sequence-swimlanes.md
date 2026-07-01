# Construction Sequence Swimlanes — Mainland High-Rise RC Tower

Reference for `cn-construction-programme`. Durations illustrative only.

---

## Swimlane Diagram (text)

```
时间 →
土方基坑    [██████░░░░░░░░░░░░░░░░░░░░]
桩基基础    [░░░░████░░░░░░░░░░░░░░░░░░]
地下室结构  [░░░░░░░░██████░░░░░░░░░░░░]
塔楼结构    [░░░░░░░░░░░░░░████████████]
幕墙        [░░░░░░░░░░░░░░░░░████████]
机电安装    [░░░░░░░░░░░░░░░░░░░██████]
精装验收    [░░░░░░░░░░░░░░░░░░░░░░████]
```

---

## Interface Rules

1. **幕墙** follows structure by N floors (project-specific lag).
2. **样板层**验收后标准层展开。
3. **消防**管道试压 before ceiling close in each zone.
4. **装配式** add module hoist lane and stacking yard on critical path.

---

## Hold Points (typical)

| Node | Lane |
|------|------|
| 垫层验收 | 土方 |
| 底板防水 | 地下 |
| 标准层验收 | 结构 |
| 幕墙四性试验 | 幕墙 |
| 消防联动 | 机电 |
