// filepath: /hike-tracker-app/hike-tracker-app/src/models/index.ts
export interface Hike {
    id: number;
    date: Date;
    location: string;
    distance: number; // in kilometers
    duration: number; // in minutes
    equipment: Equipment[];
}

export interface Equipment {
    id: number;
    name: string;
    type: string; // e.g., "tent", "backpack", "clothing"
    weight: number; // in grams
    quantity: number;
}