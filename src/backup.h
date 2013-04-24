/* backup.h - definitions for the backup type
 *
 * Copyright (C) 2010 Gerhard H�ring <gh@ghaering.de>
 *
 * This file is part of pysqlite.
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the authors be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

#ifndef PYSQLITE4_BACKUP_H
#define PYSQLITE4_BACKUP_H
#include "Python.h"

#include "sqlite4.h"
#include "connection.h"

typedef struct
{
    PyObject_HEAD
    sqlite4_backup* backup;
    pysqlite_Connection* source_con;
    pysqlite_Connection* dest_con;
} pysqlite_Backup;

extern PyTypeObject pysqlite_BackupType;

int pysqlite_backup_setup_types(void);

#endif
