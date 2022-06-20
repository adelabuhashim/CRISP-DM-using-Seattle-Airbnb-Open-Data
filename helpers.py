import pandas as pd
import re


def neat_display(objects):
    for _, __ in objects:
        print(_)
        display(__,)
        print(
            "______________________________________________________________________________"
        )
        print()


def list_clean(l):
    """
    
    """
    if len(l) == 0:
        l = None
    return l


def data_investigation(df):
    """
    
    
    """
    try:
        dtypes = pd.Series(
            [
                re.findall(r"<class '(.*)'>", str(type(i)))[0]
                for i in df.dropna(how="any").head(1).values[0]
            ],
            index=list(df.columns),
        )
    except:
        df_temp = df.dropna(how="all", axis=0)

        try:
            dtypes = pd.Series(
                [
                    re.findall(r"<class '(.*)'>", str(type(i)))[0]
                    for i in df_temp.dropna(how="any").head(1).values[0]
                ],
                index=list(df.columns),
            )
        except:
            dtypes = "TO BE DONE NEXT PUSH"

    a = []
    for c in df.columns:
        if df[[c]].value_counts().max() / df[[c]].shape[0] == 1:
            a.append((c, df[[c]].values[0][0]))
    to_drop_one = list_clean(a)
    if to_drop_one != None:
        to_drop_one = pd.Series([i[1] for i in a], index=[i[0] for i in a])

    to_drop_null = list(df.columns[df.isnull().mean() == 1])
    to_drop_null = list_clean(to_drop_null)

    neat_display(
        [
            ("Data Head", df.head(2)),
            (
                "Data Shape",
                f"The data has {df.shape[0]} rows and {df.shape[1]} columns",
            ),
            ("Columns", list(df.columns)),
            ("Columns Must be Dropped (ALL NULLS)", to_drop_null,),
            ("Columns Must be Dropped (HAS ONLY ONE UNIQUE VALUE)", to_drop_one,),
            ("Column Data Type", dtypes),
            ("Number of Nulls in Each Column", df.isnull().sum()),
            ("Percentge of Nulls in Each Column", df.isnull().mean()),
            ("Numeric Columns' Staticts", df.describe()),
        ]
    )
