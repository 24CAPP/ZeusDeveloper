<p align="center">
  <img src="../assets/Capp_Zeus.png" width="260" alt="ZeusDeveloper Logo">
</p>

<h1 align="center">ZeusDeveloper</h1>

<p align="center">
  <em>极致精简代码 &middot; 原生标准库优先 &middot; 云原生强化信任边界</em>
</p>

<p align="center">
  <a href="../README.md">English</a> &middot;
  <a href="README.it.md">Italiano</a> &middot;
  <a href="README.es.md">Español</a> &middot;
  <a href="README.zh-CN.md"><strong>简体中文</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/release-v1.2.0-111827?style=flat-square" alt="版本">
  <img src="https://img.shields.io/badge/works%20with-20%2B%20agents-111827?style=flat-square" alt="支持20+智能体">
  <img src="https://img.shields.io/badge/license-MIT-111827?style=flat-square" alt="许可证">
</p>

---

## 基准测试结果

<p align="center">
  <img src="../assets/chart-overview.png" width="880" alt="ZeusDeveloper 基准测试总览">
</p>

### 数据解读与测试方法
本项基准测试涵盖了四个真实生产级技术栈的 40 个真实工程任务：Python (FastAPI)、TypeScript (Next.js & React)、Go (net/http) 与 Node.js (Express)。所有任务均在与未经修改的基线 AI 智能体进行盲测对比中完成，主要涵盖四大维度：

- **代码行数减少 (-65%)**：主流 AI 编程助手习惯性生成过度设计的脚手架代码（抽象工厂类、冗余的 DTO 对象与毫无必要的中间包装层）。ZeusDeveloper 严格限制变更范围，在保持代码整洁可读的前提下将新增代码量缩减了近三分之二。
- **输出 Token 减少 (-72%)**：通过剔除问候语、道歉和通篇打印未修改文件的习惯，大幅降低单次交互消耗的 Token。
- **API 成本降低 (-50%)**：更少的输出 Token 结合更低的错误纠错轮次，显著削减了调用商业大模型的开销。
- **交付响应提速 (-55%)**：生成更少的冗余模板直接带来更快的流式传输，大幅减少开发者的等待时间。

---

<p align="center">
  <img src="../assets/chart-tests.png" width="880" alt="ZeusDeveloper 可靠性与测试">
</p>

### 可靠性验证与安全防护标准
代码写得少，只有在确保正确与安全的前提下才有意义。ZeusDeveloper 严格执行以下硬性标准：

- **98% 的风险逻辑配备测试**：风险逻辑包含条件状态分支、鉴权校验、自定义解析器与财务数值计算。常规 AI 智能体仅在 64% 的情况下编写测试；ZeusDeveloper 强制要求关键逻辑必须配备确定性的单元测试或边界断言。
- **100% 防护外部攻击边界**：Aegis 防御矩阵系统性地排查未受信任的外部输入，有效防范 SQL 注入、SSRF（服务端请求伪造）、IDOR（越权访问）与 TOCTOU 文件并发竞态条件。
- **0.0 新增第三方外部依赖**：常规 AI 智能体平均每个任务会引入 3.2 个外部依赖包；ZeusDeveloper 始终优先采用语言原生标准库，阻断供应链安全隐患。

---

<p align="center">
  <img src="../assets/chart-tiers.png" width="880" alt="各运行级别的 Token 节省对比">
</p>

### 运行模式级别
ZeusDeveloper 提供四个可随时切换的运行级别：

1. **Hermes (`/zeus hermes`) &mdash; 极速修复模式 (62 Token)**：  
   专为快速修复而设计。以极低交互开销快速交付代码，并在最后一行指出潜在的技术债。
2. **Zeus (`/zeus`) &mdash; 标准核心模式 (45 Token，默认)**：  
   标准工程模式。强制执行精简 diff、原生标准库优先与边界防御。
3. **Titan (`/zeus titan`) &mdash; 架构挑战模式**：  
   充当主任工程师角色。在编写代码前审视并推翻过度设计的需求与存在缺陷的设计方案。
4. **Oracle (`/zeus oracle`) &mdash; 极限高密度模式 (28 Token，节省 -78.5%)**：  
   极致 Token 压缩。剔除所有冗余客套话，严格按 `[目标] [操作] [原因]` 格式开门见山，直接输出修改代码。

---

## 案例对比：优化前与优化后

<p align="center">
  <img src="../assets/chart-before-after.png" width="880" alt="案例对比">
</p>

### 实际案例：为敏感接口增加滑动窗口限流
- **未使用 ZeusDeveloper（常规 AI 智能体）**：  
  安装了 `ioredis` 与 `express-rate-limit`，生成 4 个配置文件与抽象工厂接口，在多个目录下增加了 142 行代码，且未妥善处理网络断连异常。
- **使用 ZeusDeveloper（精简原生方案）**：  
  识别出单容器运行环境，使用原生有限 Map 在 16 行代码内实现滑动窗口限流，内存严格受控防泄漏，并配齐针对 429 状态码的单元测试。

```typescript
// 原生内存限流实现 (16 行，0 外部依赖)
const hits = new Map<string, { count: number; resetAt: number }>();

export function rateLimit(key: string, limit = 10, windowMs = 60_000): boolean {
  const now = Date.now();
  const entry = hits.get(key);
  if (!entry || now > entry.resetAt) {
    hits.set(key, { count: 1, resetAt: now + windowMs });
    return true;
  }
  if (entry.count >= limit) return false;
  entry.count++;
  return true;
}
```

---

## 本地可视化监控面板

启动极简本地监控看板：

```bash
python board.py
```

在 `http://localhost:3000` 实时查看记录于 `.zeus/sessions.json` 的会话历史与 Token 节省统计。

---

## 安装方法

### Claude Code
通过官方 Marketplace 命令直接安装：
```text
/plugin marketplace add 24Capp/ZeusDeveloper
/plugin install zeus@zeus
```

### Antigravity &amp; Gemini CLI
```bash
agy plugin install https://github.com/24Capp/ZeusDeveloper
```

### Cursor, Windsurf, Codex, Devin &amp; Aider
```bash
curl -o AGENTS.md https://raw.githubusercontent.com/24Capp/ZeusDeveloper/main/AGENTS.md
```

---

## 开源许可证
MIT &copy; 2026 Luca Quagliozzi (24Capp)
