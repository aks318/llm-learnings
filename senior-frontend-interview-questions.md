# Senior Frontend Developer — Interview Questions Roadmap

A concise, interview-focused checklist for a senior frontend developer, especially with React, Next.js, TypeScript, and production web applications.

Use each question as a speaking prompt. Practise answering in **1–3 minutes**, then give a real example or trade-off.

## 1. Browser and Web Fundamentals
- [ ] What happens after you enter a URL in the browser and press Enter?
- [ ] How does DNS resolution work?
- [ ] What are TCP, TLS, and HTTPS?
- [ ] How does the browser request and receive data from a server?
- [ ] What are HTTP methods and status codes?
- [ ] What is the difference between HTTP/1.1, HTTP/2, and HTTP/3?
- [ ] What happens after the browser receives HTML, CSS, and JavaScript?
- [ ] What are the DOM and CSSOM?
- [ ] Explain the browser rendering pipeline: style, layout, paint, and compositing.
- [ ] What causes reflow and repaint?
- [ ] What is the event loop? Explain tasks and microtasks.
- [ ] What are cookies, localStorage, sessionStorage, and IndexedDB?
- [ ] What is CORS, and why does a preflight request happen?
- [ ] What is browser caching? Explain Cache-Control and ETag.
- [ ] What is the difference between cookies and bearer tokens for authentication?

## 2. Frontend Performance and Optimization
- [ ] What techniques do you use to optimize a frontend application?
- [ ] How do you identify what is making a page slow?
- [ ] What are Core Web Vitals: LCP, INP, and CLS?
- [ ] How do you reduce JavaScript bundle size?
- [ ] What are code splitting, lazy loading, and tree shaking?
- [ ] What is route-based code splitting?
- [ ] How do you optimize images and fonts?
- [ ] What are preload, prefetch, and preconnect?
- [ ] How do you reduce unnecessary React re-renders?
- [ ] When should you use React.memo, useMemo, and useCallback?
- [ ] How do you optimize a page that renders thousands of rows?
- [ ] What is list virtualization, and when would you use it?
- [ ] What causes memory leaks in frontend applications?
- [ ] How do you find and fix layout thrashing?
- [ ] How do you optimize API calls and avoid request waterfalls?
- [ ] When should you debounce or throttle an event?
- [ ] When would you use a Web Worker?
- [ ] How do you measure whether an optimization worked?

## 3. JavaScript Essentials
- [ ] What is a closure, and where have you used one?
- [ ] Explain var, let, and const.
- [ ] What is hoisting and the temporal dead zone?
- [ ] How does this work in JavaScript?
- [ ] What is the difference between == and ===?
- [ ] Explain shallow copy vs. deep copy.
- [ ] What is the difference between promises and async/await?
- [ ] How does Promise.all differ from Promise.allSettled?
- [ ] What are the call stack, task queue, and microtask queue?
- [ ] What is event delegation?
- [ ] What are debounce and throttle? How would you implement each?
- [ ] What is a race condition in frontend code?
- [ ] How do you cancel an in-flight fetch request?
- [ ] What are memory leaks, and how do you debug them?
- [ ] What are ES modules and dynamic imports?

## 4. React
- [ ] What causes a React component to re-render?
- [ ] How does React reconciliation work?
- [ ] Why are stable keys important in lists?
- [ ] What are the Rules of Hooks?
- [ ] When should you use useEffect?
- [ ] Why can an effect run more often than expected?
- [ ] What is a stale closure?
- [ ] useRef vs. useState: when do you use each?
- [ ] useMemo vs. useCallback: what is the difference?
- [ ] What is React Context, and when can it hurt performance?
- [ ] How do you choose between local state, Context, and Redux/Zustand?
- [ ] Controlled vs. uncontrolled components: what is the difference?
- [ ] How do you handle errors in a React application?
- [ ] What are Error Boundaries, and what do they not catch?
- [ ] What is Suspense used for?
- [ ] How do you prevent unnecessary re-renders?
- [ ] How would you optimize a large form or data table?
- [ ] How do you structure a reusable component API?
- [ ] What are common mistakes when building custom hooks?

## 5. Next.js and Rendering
- [ ] Why use Next.js instead of a plain React SPA?
- [ ] CSR vs. SSR vs. SSG vs. ISR: what is the difference?
- [ ] How do you choose the right rendering strategy for a page?
- [ ] What is hydration, and what causes hydration mismatches?
- [ ] What are Server Components and Client Components?
- [ ] When should a component use the 'use client' directive?
- [ ] How do you keep secrets out of the browser bundle?
- [ ] How does caching work in the Next.js version you use?
- [ ] How do you revalidate or invalidate cached data?
- [ ] What are layouts, loading UI, error UI, and route groups?
- [ ] How do you handle authentication and authorization in Next.js?
- [ ] How do you optimize metadata, images, fonts, and scripts?
- [ ] What is streaming SSR, and how does Suspense help?
- [ ] How do you investigate a slow Next.js route?

## 6. API and Data Fetching
- [ ] What happens when fetch() is called from the browser?
- [ ] How do you handle loading, success, empty, and error states?
- [ ] How do you prevent race conditions in search requests?
- [ ] How do you cancel an API request with AbortController?
- [ ] When should you retry a failed request?
- [ ] How do you implement exponential backoff?
- [ ] How do you avoid duplicate API calls?
- [ ] What is the difference between offset and cursor pagination?
- [ ] How do you implement optimistic updates safely?
- [ ] How do you handle expired authentication sessions?
- [ ] REST vs. GraphQL: what are the trade-offs?
- [ ] WebSockets vs. Server-Sent Events vs. polling: when would you use each?
- [ ] How do you handle reconnects and duplicate real-time events?
- [ ] How do you validate API responses at runtime with TypeScript?

## 7. HTML, CSS, and Accessibility
- [ ] Why is semantic HTML important?
- [ ] Flexbox vs. Grid: when do you use each?
- [ ] How does CSS specificity work?
- [ ] What creates a stacking context?
- [ ] How do you build responsive layouts?
- [ ] What are CSS containment and container queries?
- [ ] How do you avoid CSS conflicts in a large application?
- [ ] How do you make a dialog keyboard-accessible?
- [ ] What is the difference between a button and a link?
- [ ] What are ARIA attributes, and when should you avoid them?
- [ ] How do you test keyboard and screen-reader accessibility?
- [ ] How can animations affect performance and accessibility?

## 8. Frontend Architecture
- [ ] How do you structure a large React application?
- [ ] Feature-based vs. layer-based folder structure: what are the trade-offs?
- [ ] How do you decide what should become a shared component?
- [ ] What makes a component reusable without overengineering it?
- [ ] How do you separate UI, business logic, and data access?
- [ ] How do you prevent circular dependencies?
- [ ] What are design systems and design tokens?
- [ ] What are micro frontends, and when are they justified?
- [ ] What are the challenges of shared dependencies in micro frontends?
- [ ] How do you manage shared state across independently deployed modules?
- [ ] How do you document an important architecture decision?
- [ ] How do you reduce technical debt without a risky rewrite?

## 9. Security
- [ ] What is XSS, and how do you prevent it?
- [ ] What is CSRF, and how do you mitigate it?
- [ ] Why is CORS not an authentication mechanism?
- [ ] How do CSP headers help?
- [ ] Why must API secrets never be placed in frontend code?
- [ ] How should authentication tokens and session cookies be handled?
- [ ] Why must authorization be enforced on the server?
- [ ] How do you safely render untrusted Markdown or HTML?
- [ ] How do you reduce dependency and supply-chain risks?

## 10. Testing and Delivery
- [ ] Unit vs. integration vs. end-to-end tests: what is the difference?
- [ ] What should you test in a React component?
- [ ] How do you test API loading and error states?
- [ ] How do you test a debounce, timer, or retry?
- [ ] How do you test accessibility?
- [ ] What causes flaky tests, and how do you fix them?
- [ ] What should run in CI before a deployment?
- [ ] How do you manage environment variables safely?
- [ ] How do you release a risky change safely?
- [ ] What are feature flags and rollback strategies?

## 11. Production Debugging
- [ ] A page is slow only in production. How do you investigate?
- [ ] A component re-renders continuously. How do you debug it?
- [ ] A user sees stale data. Where would you look?
- [ ] How do you investigate frontend JavaScript errors?
- [ ] What are source maps, and how should they be handled?
- [ ] What frontend metrics should be monitored?
- [ ] How do you correlate frontend failures with backend requests?
- [ ] How do you prevent sensitive data from appearing in logs?

## 12. Senior-Level Scenarios
- [ ] How would you optimize a React dashboard with a large data table?
- [ ] How would you design a frontend for millions of records?
- [ ] How would you handle a slow backend without freezing the UI?
- [ ] How would you migrate a large JavaScript application to TypeScript?
- [ ] How would you split a monolithic frontend into modules?
- [ ] How would you improve the performance of an existing production app?
- [ ] How would you choose between fixing technical debt and delivering a feature?
- [ ] How would you review a pull request that works but is difficult to maintain?
- [ ] How would you investigate a bug that only affects some users?
- [ ] Describe a technical decision you made, the alternatives, and the trade-offs.
- [ ] Describe a production issue you solved and how you prevented recurrence.
- [ ] How do you mentor developers and raise code quality across a team?

## High-Priority Revision Order
1. **Browser lifecycle:** URL → DNS → connection/TLS → HTTP request/response → HTML parsing → DOM/CSSOM → render → JavaScript execution.
2. **Optimization:** Core Web Vitals, bundle splitting, lazy loading, image optimization, caching, React profiling, virtualization.
3. **React:** re-renders, hooks, effects, stale closures, state management, memoization.
4. **Next.js:** rendering strategies, hydration, Server/Client Components, caching, security.
5. **API handling:** loading/error states, cancellation, race conditions, retries, pagination, real-time updates.
6. **Architecture:** feature boundaries, reusable components, micro frontends, trade-offs.
7. **Security, accessibility, testing, and production debugging.

## Interview Answer Formula
For technical questions, structure answers like this:
1. **What it is**
2. **Why it matters**
3. **How it works**
4. **When you would use it**
5. **Trade-offs or a real project example**

For optimization questions, add: **measure the baseline → identify the bottleneck → apply the smallest effective fix → measure again**.
