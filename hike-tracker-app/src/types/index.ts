// filepath: /hike-tracker-app/hike-tracker-app/src/types/index.ts
export interface HikeType {
    id: string;
    date: Date;
    location: string;
    duration: number; // in minutes
    distance: number; // in kilometers
    equipmentUsed: string[];
}

export interface EquipmentType {
    id: string;
    name: string;
    category: string; // e.g., clothing, gear, food
    quantity: number;
    condition: string; // e.g., new, used, needs repair
}