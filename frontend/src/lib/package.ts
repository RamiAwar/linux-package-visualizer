export interface Constraint {
    version_constraint: string;
}

export interface Dependency {
    name: string;
}

export type DependencyTuple = [Dependency, Constraint];

export interface Package {
    name: string;
    status: string;
    maintainer: string;
    version: string;
    description: string;
    depends?: DependencyTuple[];
    reverse_depends?: DependencyTuple[];
    alts?: DependencyTuple[];
    conflicts?: DependencyTuple[];
    suggests?: string[];
    priority?: string;
    section?: string;
    installed_size?: number;
    architecture?: string;
    homepage?: string;
}