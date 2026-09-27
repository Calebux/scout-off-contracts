"use strict";
// COMPILED OUTPUT — do not edit. Generated from tests/middleware/tokenRevocation.test.ts
// This file is a compiled artifact and should NOT be tracked in git.
Object.defineProperty(exports, "__esModule", { value: true });
const auth_1 = require("../../dist/middleware/auth");
describe("tokenRevocation", () => {
    it("rejects revoked tokens", () => {
        const req = { headers: { authorization: "Bearer revoked.token.here" } };
        const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
        (0, auth_1.authMiddleware)(req, res, jest.fn());
        expect(res.status).toHaveBeenCalledWith(401);
    });
});
