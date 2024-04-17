
// input types for configuration form
export type BaseInputProps = {
    name: string;
    type: string;
    description: string;
    label: string;
};

export type SelectInputProps = BaseInputProps & {
    values: string[];
    defaultValue: string;
    onChange: (
        name: string, 
        value: string
    ) => void;
};

export type CheckInputProps = BaseInputProps;

export type NumberInputProps = BaseInputProps & {
    min: number;
    max: number;
    step: number;
    defaultValue: number;
    onChange: (
        name: string, 
        value: number
    ) => void;
};

export type DialogProps = {
    propName: string;
    propDescription: string;
}
export type LinerProgressProp = {
    value: number;
};

export type HistoryRowProps = {
    id: number;
    model: string;
    dataset: string;
    date: string;
    precision: number;
    recall: number;
    f1: number;
};

export type ResultProps = {
    attackClass: string;
    precision: number;
    recall: number;
    f1: number;
    support: number;
}

export type ModelSubResultProps = {
    evaluationMatrix: string;
    value: number;
}

export type ClassSubResultProps = {
    class: string;
    value: number;
}

