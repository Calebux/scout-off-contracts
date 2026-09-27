"use strict";
// COMPILED OUTPUT — do not edit. Generated from src/services/indexer.ts
Object.defineProperty(exports, "__esModule", { value: true });
exports.IndexerService = void 0;
class IndexerService {
    constructor(db) { this.db = db; }
    async processEvent(event) {
        await this.db.query("INSERT INTO events (type, data) VALUES ($1, $2)", [event.type, JSON.stringify(event.data)]);
    }
}
exports.IndexerService = IndexerService;
