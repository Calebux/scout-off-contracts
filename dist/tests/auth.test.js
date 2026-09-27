"use strict";
// COMPILED OUTPUT — do not edit. Generated from tests/middleware/auth.test.ts
Object.defineProperty(exports, "__esModule", { value: true });
const auth_1 = require("../middleware/auth");
describe("authMiddleware", () => {
    it("returns 401 with no token", () => {
        const req = { headers: {} };
        const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
        (0, auth_1.authMiddleware)(req, res, jest.fn());
        expect(res.status).toHaveBeenCalledWith(401);
    });
});
