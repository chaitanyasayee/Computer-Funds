| Feature           | Monolith               | Microservices                                      |
| ----------------- | ---------------------- | -------------------------------------------------- |
| Structure         | Single codebase        | Multiple independent services                      |
| Scalability       | Entire app             | Per service                                        |
| Deployment        | One unit               | Independently                                      |
| Tech Stack        | Uniform                | Can be mixed per service                           |
| Failure impact    | Affects entire app     | Localized to a service                             |
| Development speed | Fast early, slow later | Slower start, scales better later                  |
| InfraCost         | cheaper                | Costlier as services increases                     |
| Testing           | Comparitively easy     | its a slightly difficult to write end-end testcase |

## Product Requirements

### Authentication

- **Create Account**
  Allow users to sign up with basic details and secure authentication.
- **Login**
  Validate user credentials and provide an access token (JWT or session-based).

### User Profile

- **Update Profile**
  Users can edit details like preferred name, gender, age, etc.

### Explore Feed

- **Feed Page**
  Explore other developer profiles based on filters (optional for MVP).

### Connections

- **Send Connection Request**
  Users can send connection invites to others.
- **View Duo Matches**
  List of mutually accepted connections.
- **View Requests Sent and Received**
  Show pending, accepted, rejected requests.

### Beta Feature (Optional)

- **Cheesy Lines with LLM**
  Integrate LLM (e.g., GPT) to suggest funny or interesting ice-breakers.

---

## Tech Planning

### System Design

We'll split the app into two microservices:

1. **Frontend**
   - Likely React (or Next.js) SPA for web UI.
2. **Backend**
   - REST API server.
   - Handles all core logic, authentication, and database operations.

---

## ⚙️ Backend Architecture (Deep Dive)

A well-planned backend will make development smoother and future-proof.

### 🗃️ Step 1: Database Design

We’ll use **MongoDB** for flexible schema design, as the user model may evolve.

### 1. `users` Collection

Stores user information.

```json
{
  _id: ObjectId,
  firstName: String,
  lastName: String,
  preferredName: String,
  email: String,
  passwordHash: String,
  age: Number,
  gender: String,
  createdAt: Date,
  updatedAt: Date
}

```

> Note: Passwords will be hashed using bcrypt or similar.

### 2. `connections` Collection

Stores connection requests and their statuses.

```json
{
  _id: ObjectId,
  fromUserId: ObjectId, // Sender
  toUserId: ObjectId,   // Receiver
  status: String,       // "pending", "accepted", "rejected", "ignored"
  createdAt: Date,
  updatedAt: Date
}

```

---

### Step 2: API Design

---

## Authentication Endpoints

| Method | Endpoint  | Description                |
| ------ | --------- | -------------------------- |
| POST   | `/signup` | Register a new user        |
| POST   | `/login`  | Log in and receive a token |

---

## User Profile Endpoints

| Method | Endpoint   | Description                         |
| ------ | ---------- | ----------------------------------- |
| GET    | `/profile` | Fetch the current user’s profile    |
| POST   | `/profile` | Create user profile (initial setup) |
| PATCH  | `/profile` | Update existing profile info        |
| DELETE | `/profile` | Delete current user account/profile |

> Requires authentication (token-based)

---

## Connection & Request Endpoints

| Method | Endpoint                 | Description                                       |
| ------ | ------------------------ | ------------------------------------------------- |
| POST   | `/sendRequest/ignore`    | Ignore a profile (soft rejection)                 |
| POST   | `/sendRequest/intrested` | Show interest / send a connection request         |
| POST   | `/reviewRequest/accept`  | Accept an incoming connection request             |
| POST   | `/reviewRequest/reject`  | Reject an incoming request                        |
| GET    | `/request`               | Get all requests (sent + received + pending)      |
| GET    | `/connections`           | Get all accepted mutual connections (duo matches) |

---

### LLM Integration

- Endpoint: `POST /llm/cheesy-line`
- Input: Target user's profile
- Output: AI-generated ice-breaker or message

Can be used for:

- Personalized openers
- Fun conversation starters

Here’s a **complete and structured note** combining your current content with essential backend concepts tailored to **Express.js 5** and general backend mastery. This is great for interviews, revision, or building projects.

## Creating the Server (Express.js)

```
const express = require('express');
const app = express();
const PORT = 3000;

app.get('/hello', (req, res) => {
  res.send('Hello World');
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

```

---

## Route Matching in Express

- Routes like `/hello` will match `/hello` and `/hello/anything` **if wildcards** or `app.use()` is used.
- `/helloanything` will **NOT match** `/hello`.
- **Route order matters** — more specific routes should come before general routes.

```
app.get('/hello/anything', ...); // ✅ Specific
app.get('/hello', ...); // ✅ General

```

> Always define more specific routes first, otherwise general ones will override.

---

## Why Not Test APIs in Browser?

- Browser only supports **GET** requests directly.
- Cannot test:
  - POST
  - PUT
  - DELETE
  - Auth headers
  - Body payloads
- Use **Postman**, **Thunder Client**, **Insomnia**, or **cURL**.

---

## What is `app.use()`?

- Mounts **middleware functions** at a specific path.
- Used for:
  - Middleware like logging, parsing, CORS, compression
  - Mounting routers

```
app.use(express.json()); // JSON body parser
app.use('/api', router); // Mounting a router

```

---

## What’s New in Express.js v5.0

### 1. Async Error Handling

```
app.get('/data', async (req, res) => {
  const data = await fetchData(); // Automatically forwards errors
  res.send(data);
});

```

No more `try/catch` + `next(err)`!

---

### 2. Improved Route Matching

- Uses upgraded `path-to-regexp v8`
- **Inline regex** like `/:id(\d+)` ➝ ❌ Not supported
- Use validation middleware (e.g., `express-validator`)
- ➝ Now use `(.*)`
- Optional param syntax changed:
  ```diff
  - /user/:id?
  + /user{/:id}

  ```
- Named parameters **required** — no more `req.params[0]`

---

### 3. Invalid Status Codes Throw Errors

```
res.status(978).send('Invalid'); // ❌ Throws error in Express 5

```

Only valid HTTP status codes are allowed.

---

### 4. Deprecated Methods Removed

- `app.del()` ➝ Use `app.delete()`
- `req.param()` ➝ ❌ Removed
  - Use:
    - `req.params` for URL params
    - `req.query` for query strings
    - `req.body` for request body
- Renamed methods:
  - `req.acceptsCharsets()`
  - `req.acceptsEncodings()`
  - `req.acceptsLanguages()`

---

### 5. Reintroduced `app.router`

```
const router = express.Router();
router.get('/profile', (req, res) => res.send('Profile'));
app.use('/user', router); // => /user/profile

```

Useful for **modularizing route logic**.

---

### 6. Body Parser Removed

- `bodyParser()` middleware removed (deprecated in v4 too)
- Use:

```
app.use(express.json());
app.use(express.urlencoded({ extended: false, depth: 10 }));

```

- `req.body` is undefined without these!

---

### 7. Brotli Compression Support

```
const compression = require('compression');
app.use(compression({
  brotli: { enabled: true }
}));

```

- Smaller payloads
- Faster response time

---

### 8. Node.js v18+ Required

Express 5 requires **Node.js v18 or later** due to modern features:

- `Array.flat()`
- `path.isAbsolute()`
- Top-level await (optional)

---

## Should You Upgrade?

### YES — if using Node.js v18+

Upgrade command:

```bash
npm install express@next

```

### 🔍 Run tests:

- Ensure no deprecated patterns (`req.param`, inline regex, etc.)
- Test all routes and middleware

---

## Migration Resources

- [🧭 Migration Guide](https://expressjs.com/en/guide/migrating-5.html)
- [📝 Full Docs](https://expressjs.com/)

---

## Additional Backend Concepts

### Middleware Examples

```
// Logging
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

```

---

### JWT Authentication Sample

```
const jwt = require('jsonwebtoken');

function authenticate(req, res, next) {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).send('No token');

  try {
    const user = jwt.verify(token, 'secret-key');
    req.user = user;
    next();
  } catch {
    res.status(403).send('Invalid token');
  }
}

```

---

### Route Parameters

```
app.get('/user/:id', (req, res) => {
  const userId = req.params.id;
});

```

---

### Testing API Endpoints

- Use `supertest` + `jest/mocha` for automated testing:

```
const request = require('supertest');
const app = require('./app');

test('GET /hello', async () => {
  const res = await request(app).get('/hello');
  expect(res.statusCode).toBe(200);
});

```

---
