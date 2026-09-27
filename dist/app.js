"use strict";
// COMPILED OUTPUT — do not edit. Generated from src/app.ts
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = require("express");
const auth_1 = require("./middleware/auth");
const app = (0, express_1.default)();
app.use(express_1.default.json());
app.use("/api", auth_1.authMiddleware);
app.listen(3000, () => console.log("Server running on port 3000"));
exports.default = app;
