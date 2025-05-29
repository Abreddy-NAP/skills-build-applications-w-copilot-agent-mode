// This script initializes the octofit_db database and its collections in MongoDB.

// Connect to the octofit_db database
use octofit_db;

// Create users collection with unique email index
if (!db.users.getIndexes().some(idx => idx.key && idx.key.email)) {
  db.users.createIndex({ "email": 1 }, { unique: true });
}

// Create teams collection
if (!db.teams) {
  db.createCollection("teams");
}

// Create activity collection
if (!db.activity) {
  db.createCollection("activity");
}

// Create leaderboard collection
if (!db.leaderboard) {
  db.createCollection("leaderboard");
}

// Create workouts collection
if (!db.workouts) {
  db.createCollection("workouts");
}
