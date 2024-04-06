
// input types for configuration form
export type BaseInputProps = {
    type: string;
    description: string;
    label: string;
};

export type SelectInputProps = BaseInputProps & {
    values: string[];
};

export type CheckInputProps = BaseInputProps;

export type NumberInputProps = BaseInputProps & {
    min: number;
    max: number;
    step: number;
    defaultValue: number;
};

export type DialogProps = {
    prop_name: string;
    prop_description: string;
}

export type LinerProgressProp = {
    value: number;
};

export type HistoryRowProps = {
    id: number;
    algorithm: string;
    dataset: string;
    date: string;
    precision: number;
    recall: number;
    f1: number;
};
